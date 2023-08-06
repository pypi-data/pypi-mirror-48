# -*- coding: utf-8 -*-

#    Copyright (C) 2014 Yahoo! Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import contextlib
import threading
import time

from zag import exceptions as excp
from zag.persistence.backends import impl_dir
from zag import states
from zag.tests import utils as test_utils
from zag.utils import threading_utils


@contextlib.contextmanager
def connect_close(*args):
    try:
        for a in args:
            a.connect()
        yield
    finally:
        for a in args:
            a.close()


class BoardTestMixin(object):

    @contextlib.contextmanager
    def flush(self, client):
        yield

    def close_client(self, client):
        pass

    def test_connect(self):
        self.assertFalse(self.board.connected)
        with connect_close(self.board):
            self.assertTrue(self.board.connected)

    def test_board_iter_empty(self):
        with connect_close(self.board):
            jobs_found = list(self.board.iterjobs())
            self.assertEqual([], jobs_found)

    def test_fresh_iter(self):
        with connect_close(self.board):
            self.board.post('test', test_utils.test_factory)
            jobs = list(self.board.iterjobs(ensure_fresh=True))
            self.assertEqual(1, len(jobs))

    def test_wait_timeout(self):
        with connect_close(self.board):
            self.assertRaises(excp.NotFound, self.board.wait, timeout=0.1)

    def test_wait_arrival(self):
        ev = threading.Event()
        jobs = []

        def poster(wait_post=0.2):
            if not ev.wait(test_utils.WAIT_TIMEOUT):
                raise RuntimeError("Waiter did not appear ready"
                                   " in %s seconds" % test_utils.WAIT_TIMEOUT)
            time.sleep(wait_post)
            self.board.post('test', test_utils.test_factory)

        def waiter():
            ev.set()
            it = self.board.wait(timeout=test_utils.WAIT_TIMEOUT)
            jobs.extend(it)

        with connect_close(self.board):
            t1 = threading_utils.daemon_thread(poster)
            t1.start()
            t2 = threading_utils.daemon_thread(waiter)
            t2.start()
            for t in (t1, t2):
                t.join()

        self.assertEqual(1, len(jobs))

    def test_posting_claim(self):

        with connect_close(self.board):
            with self.flush(self.client):
                self.board.post('test', test_utils.test_factory)

            self.assertEqual(1, self.board.job_count)
            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(1, len(possible_jobs))
            j = possible_jobs[0]
            self.assertEqual(states.UNCLAIMED, j.state)

            with self.flush(self.client):
                self.board.claim(j, self.board.name)

            self.assertEqual(self.board.name, self.board.find_owner(j))
            self.assertEqual(states.CLAIMED, j.state)

            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(0, len(possible_jobs))

        self.close_client(self.client)
        self.assertRaisesAttrAccess(excp.JobFailure, j, 'state')

    def test_posting_claim_consume(self):

        with connect_close(self.board):
            with self.flush(self.client):
                self.board.post('test', test_utils.test_factory)

            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(1, len(possible_jobs))
            j = possible_jobs[0]
            with self.flush(self.client):
                self.board.claim(j, self.board.name)

            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(0, len(possible_jobs))
            with self.flush(self.client):
                self.board.consume(j, self.board.name)

            self.assertEqual(0, len(list(self.board.iterjobs())))
            self.assertRaises(excp.NotFound,
                              self.board.consume, j, self.board.name)

    def test_posting_claim_abandon(self):

        with connect_close(self.board):
            with self.flush(self.client):
                self.board.post('test', test_utils.test_factory)

            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(1, len(possible_jobs))
            j = possible_jobs[0]
            with self.flush(self.client):
                self.board.claim(j, self.board.name)

            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(0, len(possible_jobs))
            with self.flush(self.client):
                self.board.abandon(j, self.board.name)

            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(1, len(possible_jobs))

    def test_posting_claim_diff_owner(self):

        with connect_close(self.board):
            with self.flush(self.client):
                self.board.post('test', test_utils.test_factory)

            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(1, len(possible_jobs))
            with self.flush(self.client):
                self.board.claim(possible_jobs[0], self.board.name)

            possible_jobs = list(self.board.iterjobs())
            self.assertEqual(1, len(possible_jobs))
            self.assertRaises(excp.UnclaimableJob, self.board.claim,
                              possible_jobs[0], self.board.name + "-1")
            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(0, len(possible_jobs))

    def test_posting_consume_wait(self):
        with connect_close(self.board):
            jb = self.board.post('test', test_utils.test_factory)
            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.board.claim(possible_jobs[0], self.board.name)
            self.board.consume(possible_jobs[0], self.board.name)
            self.assertTrue(jb.wait())

    def test_posting_no_consume_wait(self):
        with connect_close(self.board):
            jb = self.board.post('test', test_utils.test_factory)
            self.assertFalse(jb.wait(0.1))

    def test_posting_with_book(self):
        backend = impl_dir.DirBackend(conf={
            'path': self.makeTmpDir(),
        })
        backend.get_connection().upgrade()

        client, board = self.create_board(persistence=backend)
        with connect_close(board):
            with self.flush(client):
                job = board.post('test', test_utils.test_factory)
            book = job.book
            flow_detail = job.load_flow_detail()

            possible_jobs = list(board.iterjobs(only_unclaimed=True))
            self.assertEqual(1, len(possible_jobs))
            j = possible_jobs[0]
            self.assertEqual(1, len(j.book))
            self.assertEqual(book.name, j.book.name)
            self.assertEqual(book.uuid, j.book.uuid)
            self.assertEqual(book.name, j.book_name)
            self.assertEqual(book.uuid, j.book_uuid)

            flow_details = list(j.book)
            self.assertEqual(flow_detail.uuid, flow_details[0].uuid)
            self.assertEqual(flow_detail.name, flow_details[0].name)

    def test_posting_abandon_no_owner(self):

        with connect_close(self.board):
            with self.flush(self.client):
                self.board.post('test', test_utils.test_factory)

            self.assertEqual(1, self.board.job_count)
            possible_jobs = list(self.board.iterjobs(only_unclaimed=True))
            self.assertEqual(1, len(possible_jobs))
            j = possible_jobs[0]
            self.assertRaises(excp.NotFound, self.board.abandon,
                              j, j.name)
