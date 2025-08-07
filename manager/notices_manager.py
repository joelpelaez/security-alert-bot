# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import asyncio

from settings import get_message_wait_time, get_notices_fetch_wait_time
from db.notices import Notices
from ds import DataSource
from domain import Bot, Manager


class NoticesManager(Manager):
    """Manages notices data sources.

    This class is responsible for retrieving notices and validate it in a local
    database and send the new ones to the bots.

    This is the central module from this application.
    """

    _sources: list[DataSource]
    _db: Notices
    _bots: list[Bot]
    _running: bool
    _lock: asyncio.Lock
    _msg_wait_time: int
    _fetch_wait_time: int

    def __init__(self, sources: list[DataSource], db: Notices, bots: list[Bot]):
        self._sources = sources
        self._db = db
        self._bots = bots
        self._msg_wait_time = get_message_wait_time()
        self._fetch_wait_time = get_notices_fetch_wait_time()
        self._lock = asyncio.Lock()
        self._running = False

    async def lock(self):
        await self._lock.acquire()

    def on_ready(self):
        self._running = True
        self._lock.release()

    def on_terminate(self):
        self.stop()

    async def start_async(self):
        await self._loop()

    def stop(self):
        self._running = False
        pass

    async def _loop(self):
        async with self._lock:
            while self._running:
                await self._process_notices()

    async def _process_notices(self):
        for source in self._sources:
            notices = source.get_entries()

            for notice in notices:
                if not self._db.exists_announce(notice):
                    self._db.add_announce(notice)

                    # Send it for all bots
                    for bot in self._bots:
                        await bot.send_formatted_message(notice)

                    await asyncio.sleep(self._msg_wait_time)

        await asyncio.sleep(self._fetch_wait_time)
