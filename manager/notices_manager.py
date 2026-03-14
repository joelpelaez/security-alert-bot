# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) 2026 Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import asyncio
import logging

import aiohttp
from aiohttp import ClientSession

from settings import get_message_wait_time, get_notices_fetch_wait_time
from db.notices import Notices
from ds import DataSource
from domain import Bot, Manager
from settings.ds import get_base_date


_logger = logging.getLogger("manager.NoticesManager")


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
            async with aiohttp.ClientSession() as session:
                while self._running:
                    await self._process_notices(session)

    async def _process_notices(self, session: ClientSession):
        for source in self._sources:
            ds_name = source.__class__.__name__
            try:
                _logger.info("%s: data source fetching started", ds_name)
                await self._process_source(session, source)
                _logger.info("%s: data source fetching ended", ds_name)
            except Exception:
                _logger.error("%s: data source fetching failed", ds_name, exc_info=True)

        await asyncio.sleep(self._fetch_wait_time)

    async def _process_source(self, session: ClientSession, source: DataSource):
        ds_name = source.__class__.__name__

        notices = await source.get_entries(session)
        notices = sorted(notices, key=lambda n: n.pub_date, reverse=True)
        notices = list(filter(lambda n: n.pub_date >= get_base_date(), notices))

        _logger.info("%s: Found %d notices to process", ds_name, len(notices))

        for notice in notices:
            if not self._db.exists_announce(notice):
                _logger.info(
                    "%s: Notice '%s' is ready to be sent to bots",
                    ds_name,
                    notice.title,
                )
                self._db.add_announce(notice)

                # Send it for all bots
                for bot in self._bots:
                    await bot.send_formatted_message(notice)

                await asyncio.sleep(self._msg_wait_time)
