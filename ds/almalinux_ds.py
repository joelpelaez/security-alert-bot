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


async def _get_entries_with_version(
    session: ClientSession, release_version: int
) -> list[Entry]:
    """
    Retrieve the errata entries from a specific AlmaLinux release.
    """
    data = await get(
        session, f"https://errata.almalinux.org/{release_version}/errata.rss"
    )
    feed = feedparser.parse(data)
    entries = []
    for entry in feed.entries:
        entries.append(
            Entry(
                title=entry.title,
                link=entry.link,
                pub_date=struct_time_to_datetime(entry.published_parsed),
                content=entry.summary,
            )
        )
    return entries


class AlmaLinuxSecurityAnnouncesBase(DataSource):
    """AlmaLinux Security Announces data source.

    This data sources retrieves information from AlmaLinux Security Announces
    RSS link for listing latest security announcements.

    This is a base one, AlmaLinux separates each RSS per major release.

    Attributes:
        major_release (int):
          The major release number of an AlmaLinux, it must be defined in
          a subclass of this.
    """

    major_release: int

    async def get_entries(self, session: ClientSession) -> list[Entry]:
        return await _get_entries_with_version(session, self.major_release)


class AlmaLinuxSecurityAnnouncesV8DataSource(AlmaLinuxSecurityAnnouncesBase):
    def __init__(self):
        self.major_release = 8


class AlmaLinuxSecurityAnnouncesV9DataSource(AlmaLinuxSecurityAnnouncesBase):
    def __init__(self):
        self.major_release = 9


class AlmaLinuxSecurityAnnouncesV10DataSource(AlmaLinuxSecurityAnnouncesBase):
    def __init__(self):
        self.major_release = 10
