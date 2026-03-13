# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) 2026 Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import feedparser
from aiohttp import ClientSession

from conn.http import get
from domain.datasource import DataSource
from model.entry import Entry
from utils import struct_time_to_datetime


class FreeBSDPortsDataSource(DataSource):
    """FreeBSD ports VuXML data source.

    This data source only apply for FreeBSD ports, not base OS.
    For retrieve FreeBSD OS security announces, use FreeBSDDataSource instead.
    """

    async def get_entries(self, session: ClientSession) -> list[Entry]:
        data = await get(session, "https://vuxml.freebsd.org/freebsd/rss.xml")
        feed = feedparser.parse(data)
        entries = []
        for entry in feed.entries:
            entries.append(
                Entry(
                    title=entry.title,
                    content="",
                    link=entry.link,
                    pub_date=struct_time_to_datetime(entry.published_parsed),
                )
            )
        return entries
