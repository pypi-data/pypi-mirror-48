##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""IObjectMover implementation.
"""
from __future__ import absolute_import, print_function

import functools
import io
import os
import struct

from zope.interface import implementer
from ZODB.POSException import Unsupported

from ..._compat import xrange
from .._util import query_property
from ..interfaces import IObjectMover
from ..mover import AbstractObjectMover
from ..mover import metricmethod_sampled

# Important: pg8000 1.10 - 1.13, at least, can't handle prepared
# statements that take parameters but it doesn't need to because it
# prepares every statement anyway. So you must have a backup that you use
# for that driver.
# https://github.com/mfenniak/pg8000/issues/132


def to_prepared_queries(name, queries, datatypes=()):
    # Give correct datatypes for the queries, wherever possible.
    # The number of parameters should be the same or more than the
    # number of datatypes.
    # datatypes is a sequence of strings.

    # Maybe instead of having the adapter have to know about all the
    # statements that need prepared, we could keep a registry?
    if datatypes:
        assert isinstance(datatypes, (list, tuple))
        datatypes = ', '.join(datatypes)
        datatypes = ' (%s)' % (datatypes,)
    else:
        datatypes = ''

    result = []
    for q in queries:
        if not isinstance(q, str):
            # Unsupported marker
            result.append(q)
            continue

        q = q.strip()
        param_count = q.count('%s')
        rep_count = 0
        while rep_count < param_count:
            rep_count += 1
            q = q.replace('%s', '$' + str(rep_count), 1)
        stmt = 'PREPARE {name}{datatypes} AS {query}'.format(
            name=name, datatypes=datatypes, query=q
        )
        result.append(stmt)
    return result


@implementer(IObjectMover)
class PostgreSQLObjectMover(AbstractObjectMover):

    _prepare_load_current_queries = to_prepared_queries(
        'load_current',
        AbstractObjectMover._load_current_queries,
        ['BIGINT'])

    _prepare_load_current_query = query_property('_prepare_load_current')

    _load_current_query = 'EXECUTE load_current(%s)'

    _prepare_detect_conflict_queries = to_prepared_queries(
        'detect_conflicts',
        AbstractObjectMover._detect_conflict_queries)

    _prepare_detect_conflict_query = query_property('_prepare_detect_conflict')

    _detect_conflict_query = 'EXECUTE detect_conflicts'

    _move_from_temp_hf_insert_query_raw = """
        INSERT INTO object_state (zoid, tid, state_size, state)
        SELECT zoid, %s, COALESCE(LENGTH(state), 0), state
        FROM temp_store
        ON CONFLICT (zoid)
        DO UPDATE
        SET state_size = COALESCE(LENGTH(excluded.state), 0),
            tid = excluded.tid,
            state = excluded.state
    """

    _move_from_temp_hf_insert_raw_queries = (
        Unsupported("States accumulate in history-preserving mode"),
        _move_from_temp_hf_insert_query_raw,
    )

    _prepare_move_from_temp_hf_insert_queries = to_prepared_queries(
        'move_from_temp',
        _move_from_temp_hf_insert_raw_queries,
        ('BIGINT',)
    )

    _prepare_move_from_temp_hf_insert_query = query_property(
        '_prepare_move_from_temp_hf_insert')

    _move_from_temp_hf_insert_queries = (
        Unsupported("States accumulate in history-preserving mode"),
        'EXECUTE move_from_temp(%s)'
    )

    _move_from_temp_hf_insert_query = query_property('_move_from_temp_hf_insert')

    on_load_opened_statement_names = ('_prepare_load_current_query',)
    on_store_opened_statement_names = on_load_opened_statement_names + (
        '_prepare_detect_conflict_query',
        '_prepare_move_from_temp_hf_insert_query',
    )


    @metricmethod_sampled
    def on_store_opened(self, cursor, restart=False):
        """Create the temporary tables for storing objects"""
        # note that the md5 column is not used if self.keep_history == False.
        # Ideally we wouldn't execute any of these on a restart, but
        # I've seen an issue with temp_stare apparently going missing on pg8000
        ddl_stmts = [
            """
            CREATE TEMPORARY TABLE IF NOT EXISTS temp_store (
                zoid        BIGINT NOT NULL PRIMARY KEY,
                prev_tid    BIGINT NOT NULL,
                md5         CHAR(32),
                state       BYTEA
            ) ON COMMIT DELETE ROWS;
            """,
            """
            CREATE TEMPORARY TABLE IF NOT EXISTS temp_blob_chunk (
                zoid        BIGINT NOT NULL,
                chunk_num   BIGINT NOT NULL,
                chunk       OID,
                PRIMARY KEY (zoid, chunk_num)
            ) ON COMMIT DELETE ROWS;
            """,
        ]
        if not restart:
            ddl_stmts += [
                """
                -- This trigger removes blobs that get replaced before being
                -- moved to blob_chunk.  Note that it is never called when
                -- the temp_blob_chunk table is being dropped or truncated.
                CREATE TRIGGER temp_blob_chunk_delete
                    BEFORE DELETE ON temp_blob_chunk
                    FOR EACH ROW
                    EXECUTE PROCEDURE temp_blob_chunk_delete_trigger();
                """,
            ]
            # For some reason, preparing the INSERT statement also wants
            # to acquire a lock. If we're committing is another
            # transaction, this can block indefinitely (if that other transaction
            # happens to be in this same thread!)
            # checkIterationIntraTransaction (PostgreSQLHistoryPreservingRelStorageTests)
            # easily triggers this. Fortunately, I don't think this
            # is a common case, and we can workaround the test failure by
            # only prepping this in the store connection.
            # TODO: Is there a more general solution?
            cursor.execute('SET lock_timeout = 100')

        for stmt in ddl_stmts:
            cursor.execute(stmt)

        AbstractObjectMover.on_store_opened(self, cursor, restart)

    def _move_from_temp_object_state(self, cursor, tid):
        # Override the history-free version of moving from
        # temp_store to do it in one step.
        stmt = self._move_from_temp_hf_insert_query
        cursor.execute(stmt, (tid,))

    @metricmethod_sampled
    def store_temp(self, _cursor, batcher, oid, prev_tid, data):
        suffix = """
        ON CONFLICT (zoid) DO UPDATE SET state = excluded.state,
                              prev_tid = excluded.prev_tid,
                              md5 = excluded.md5
        """
        self._generic_store_temp(batcher, oid, prev_tid, data, suffix=suffix)

    @metricmethod_sampled
    def restore(self, cursor, batcher, oid, tid, data):
        """Store an object directly, without conflict detection.

        Used for copying transactions into this database.
        """
        self._generic_restore(batcher, oid, tid, data)

    @metricmethod_sampled
    def download_blob(self, cursor, oid, tid, filename):
        """Download a blob into a file."""
        stmt = """
        SELECT chunk_num, chunk
        FROM blob_chunk
        WHERE zoid = %s
            AND tid = %s
        ORDER BY chunk_num
        """

        f = None
        bytecount = 0
        read_chunk_size = self.blob_chunk_size

        try:
            cursor.execute(stmt, (oid, tid))
            for chunk_num, loid in cursor.fetchall():

                blob = cursor.connection.lobject(loid, 'rb')

                if chunk_num == 0:
                    # Use the native psycopg2 blob export functionality
                    blob.export(filename)
                    blob.close()
                    bytecount = os.path.getsize(filename)
                    continue

                if f is None:
                    f = open(filename, 'ab') # Append, chunk 0 was an export

                reader = iter(functools.partial(blob.read, read_chunk_size), b'')
                for read_chunk in reader:
                    f.write(read_chunk)
                    bytecount += len(read_chunk)
                blob.close()
        except:
            if f is not None:
                f.close()
                os.remove(filename)
            raise

        if f is not None:
            f.close()
        return bytecount

    # PostgreSQL < 9.3 only supports up to 2GB of data per BLOB.
    # Even above that, we can only use larger blobs on 64-bit builds.
    postgresql_blob_chunk_maxsize = 1 << 31

    @metricmethod_sampled
    def upload_blob(self, cursor, oid, tid, filename):
        """Upload a blob from a file.

        If serial is None, upload to the temporary table.
        """
        # pylint:disable=too-many-branches,too-many-locals
        if tid is not None:
            if self.keep_history:
                delete_stmt = """
                DELETE FROM blob_chunk
                WHERE zoid = %s AND tid = %s
                """
                cursor.execute(delete_stmt, (oid, tid))
            else:
                delete_stmt = "DELETE FROM blob_chunk WHERE zoid = %s"
                cursor.execute(delete_stmt, (oid,))

            use_tid = True
            insert_stmt = """
            INSERT INTO blob_chunk (zoid, tid, chunk_num, chunk)
            VALUES (%(oid)s, %(tid)s, %(chunk_num)s, %(loid)s)
            """

        else:
            use_tid = False
            delete_stmt = "DELETE FROM temp_blob_chunk WHERE zoid = %s"
            cursor.execute(delete_stmt, (oid,))

            insert_stmt = """
            INSERT INTO temp_blob_chunk (zoid, chunk_num, chunk)
            VALUES (%(oid)s, %(chunk_num)s, %(loid)s)
            """

        blob = None

        maxsize = self.postgresql_blob_chunk_maxsize
        filesize = os.path.getsize(filename)
        write_chunk_size = self.blob_chunk_size

        if filesize <= maxsize:
            # File is small enough to fit in one chunk, just use
            # psycopg2 native file copy support
            blob = cursor.connection.lobject(0, 'wb', 0, filename)
            blob.close()
            params = dict(oid=oid, chunk_num=0, loid=blob.oid)
            if use_tid:
                params['tid'] = tid
            cursor.execute(insert_stmt, params)
            return

        # We need to divide this up into multiple chunks
        f = open(filename, 'rb')
        try:
            chunk_num = 0
            while True:
                blob = cursor.connection.lobject(0, 'wb')
                params = dict(oid=oid, chunk_num=chunk_num, loid=blob.oid)
                if use_tid:
                    params['tid'] = tid
                cursor.execute(insert_stmt, params)

                for _i in xrange(maxsize // write_chunk_size):
                    write_chunk = f.read(write_chunk_size)
                    if not blob.write(write_chunk):
                        # EOF.
                        return
                if not blob.closed:
                    blob.close()
                chunk_num += 1
        finally:
            f.close()
            if blob is not None and not blob.closed:
                blob.close()

    def store_temps(self, cursor, state_oid_tid_iter):
        # History-preserving storages need the md5 to compare states.
        # We could calculate that on the server using pgcrypto, if its
        # available. Or we could just compare directly, instead of comparing
        # md5; that's fast on PostgreSQL.
        if state_oid_tid_iter:
            buf = TempStoreCopyBuffer(state_oid_tid_iter,
                                      self._compute_md5sum if self.keep_history else None)
            cursor.copy_expert(buf.COPY_COMMAND, buf)


class PG8000ObjectMover(PostgreSQLObjectMover):
    # Delete the statements that need paramaters.
    on_load_opened_statement_names = ()
    on_store_opened_statement_names = ('_prepare_detect_conflict_query',)

    _load_current_query = AbstractObjectMover._load_current_query

    _move_from_temp_hf_insert_queries = (
        Unsupported("States accumulate in history-preserving mode"),
        PostgreSQLObjectMover._move_from_temp_hf_insert_query_raw
    )


class TempStoreCopyBuffer(io.BufferedIOBase):
    """
    A binary file-like object for putting data into
    ``temp_store``.
    """

    # pg8000 uses readinto(); psycopg2 uses read().

    COPY_COMMAND = "COPY temp_store (zoid, prev_tid, md5, state) FROM STDIN WITH (FORMAT binary)"

    def __init__(self, state_oid_tid_iterable, digester):
        super(TempStoreCopyBuffer, self).__init__()
        self.state_oid_tid_iterable = state_oid_tid_iterable
        self._iter = iter(state_oid_tid_iterable)
        self._digester = digester
        if digester and bytes is not str:
            # On Python 3, this outputs a str, but our protocol needs bytes
            self._digester = lambda s: digester(s).encode("ascii")
        if self._digester:
            self._read_tuple = self._read_one_tuple_md5
        else:
            self._read_tuple = self._read_one_tuple_no_md5

        self._done = False
        self._header = self.HEADER
        self._buffer = bytearray(8192)


    SIGNATURE = b'PGCOPY\n\xff\r\n\0'
    FLAGS = struct.pack("!i", 0)
    EXTENSION_LEN = struct.pack("!i", 0)
    HEADER = SIGNATURE + FLAGS + EXTENSION_LEN
    # All tuples begin with their length in 16 signed bits, which is the same for all tuples
    # (zoid, prev_tid, md5, state)
    _common = "!hiqiqi"
    WITH_SUM = struct.Struct(_common + "32si")
    NO_SUM = struct.Struct(_common + "i")
    # Each column in the tuple is a 32-bit length (-1
    # for NULL), followed by exactly that many bytes of data.
    # Each column datum is written in binary format; for character
    # fields (like md5) that turns out to be a direct dump of the ascii.
    # For BIGINT fields, that's an 8-byte big-endian encoding
    # For BYTEA fields, it's just the raw data
    # Finally, the trailer is a tuple size of -1
    TRAILER = struct.pack("!h", -1)

    def read(self, size=-1):
        # We don't handle "read everything in one go".
        # assert size is not None and size > 0
        if self._done:
            return b''

        if len(self._buffer) < size:
            self._buffer.extend(bytearray(size - len(self._buffer)))

        count = self.readinto(self._buffer)
        if not count:
            return b''
        return bytes(self._buffer)

    def readinto(self, buf):
        # We basically ignore the size of the buffer,
        # writing more into it if we need to.
        if self._done:
            return 0

        requested = len(buf)
        # bytearray.clear() is only in Python 3
        del buf[:]

        buf.extend(self._header)
        self._header = b''

        while len(buf) < requested:
            try:
                self._read_tuple(buf)
            except StopIteration:
                buf.extend(self.TRAILER)
                self._done = True
                break

        return len(buf)

    def __len__(self):
        return len(self.state_oid_tid_iterable)

    def _read_one_tuple_md5(self,
                            buf,
                            _pack_into=WITH_SUM.pack_into,
                            _header_size=WITH_SUM.size,
                            _blank_header=bytearray(WITH_SUM.size)):

        data, oid_int, tid_int = next(self._iter)
        len_data = len(data)
        md5 = self._digester(data)
        offset = len(buf)
        buf.extend(_blank_header)
        _pack_into(
            buf, offset,
            4,
            8, oid_int,
            8, tid_int,
            32, md5,
            len_data
        )
        buf.extend(data)

    def _read_one_tuple_no_md5(self,
                               buf,
                               _pack_into=NO_SUM.pack_into,
                               _header_size=NO_SUM.size,
                               _blank_header=bytearray(NO_SUM.size)):
        data, oid_int, tid_int = next(self._iter)
        len_data = len(data)
        offset = len(buf)
        buf.extend(_blank_header)
        _pack_into(
            buf, offset,
            4,
            8, oid_int,
            8, tid_int,
            -1,
            len_data
        )
        buf.extend(data)
