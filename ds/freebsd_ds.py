# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.
from datetime import date, datetime

import feedparser
import dateparser

from domain.datasource import DataSource
from model.entry import Entry


def parse_date(data: str | date | datetime) -> datetime | None:
    if isinstance(data, date):
        return datetime(data.year, data.month, data.day)

    if isinstance(data, datetime):
        return data

    if isinstance(data, str):
        try:
            # First try parse as ISO date format
            return datetime.fromisoformat(data)
        except ValueError:
            pass

        # Try using dateparser, if it fails returns None
        return dateparser.parse(data)


class FreeBSDDataSource(DataSource):
    """FreeBSD base and kernel security advertisement and errata notices data source.

    This data sources retrieves information about FreeBSD base system security
    advertisements and errata notices from the official RSS source.
    """

    def get_entries(self) -> list[Entry]:
        feed = feedparser.parse("https://www.freebsd.org/security/rss.xml")
        entries = []
        for entry in feed.entries:
            entries.append(
                Entry(
                    title=entry.title,
                    content=entry.summary,
                    link=entry.link,
                    pub_date=parse_date(entry.published),
                )
            )
        return entries
