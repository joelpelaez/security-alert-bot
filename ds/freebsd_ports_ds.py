# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import feedparser

from domain.datasource import DataSource
from model.entry import Entry


class FreeBSDPortsDataSource(DataSource):
    """Debian DSA notices data source"""

    def get_entries(self) -> list[Entry]:
        feed = feedparser.parse("https://vuxml.freebsd.org/freebsd/rss.xml")
        entries = []
        for entry in feed.entries:
            entries.append(
                Entry(
                    title=entry.title,
                    content="",
                    link=entry.link,
                    pub_date=entry.published,
                )
            )
        return entries
