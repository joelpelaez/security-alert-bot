#!/usr/bin/env python
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
import os

import config  # noqa: F401
import setup_logger  # noqa: F401

from bot import DiscordBot
from domain import Bot
from fixtures import patch_getaddrinfo
from settings import get_data_sources
from db import get_connection, Notices, prepare_database
from manager import NoticesManager


def create_discord_bot() -> DiscordBot:
    token = os.getenv("DISCORD_TOKEN")
    channel_id = int(os.getenv("DISCORD_CHANNEL"))
    return DiscordBot(token, channel_id)


def create_notices_manager(bot: Bot) -> NoticesManager:
    dss = [ds() for ds in get_data_sources()]
    conn = get_connection()
    db = Notices(conn)
    bots = [bot]
    manager = NoticesManager(dss, db, bots)
    return manager


async def tasks():
    bot = create_discord_bot()
    manager = create_notices_manager(bot)
    bot.register_manager(manager)

    async def bot_runner():
        await bot.start_async()

    async def announces_runner():
        # Start locked awaiting the bot be ready
        await manager.lock()
        await manager.start_async()

    await asyncio.gather(bot_runner(), announces_runner())


def start_loop():
    try:
        asyncio.run(tasks())
    except KeyboardInterrupt:
        return


def main():
    if os.environ.get("DISABLE_IPV6") == "True":
        patch_getaddrinfo()

    prepare_database()

    start_loop()


if __name__ == "__main__":
    main()
