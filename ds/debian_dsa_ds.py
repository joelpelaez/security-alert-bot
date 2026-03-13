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
import html_to_markdown
from aiohttp import ClientSession
from html_to_markdown import ConversionOptions

from conn.http import get
from domain.datasource import DataSource
from model.entry import Entry
from utils import struct_time_to_datetime


def convert_from_html(html: str) -> str:
    """Convert an HTML string to Markdown

    Convert the HTML entry to Markdown compatible with Discord.
    """
    options = ConversionOptions()
    return html_to_markdown.convert(html, options)


class DebianDSADataSource(DataSource):
    """Debian Security Advisories data source.

    This data sources retrieves information from Debian Security Advisories
    RSS link for listing latest security announcements.
    """

    async def get_entries(self, session: ClientSession) -> list[Entry]:
        data = await get(session, "https://www.debian.org/security/dsa-long.rdf")
        feed = feedparser.parse(data)
        entries = []
        for entry in feed.entries:
            entries.append(
                Entry(
                    title=entry.title,
                    link=entry.link,
                    pub_date=struct_time_to_datetime(entry.updated_parsed),
                    content=convert_from_html(entry.summary),
                )
            )
        return entries
