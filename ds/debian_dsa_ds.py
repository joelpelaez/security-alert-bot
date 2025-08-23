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
import html_to_markdown
from bs4 import Tag

from domain.datasource import DataSource
from model.entry import Entry


def process_a_tag(text: str, tag: Tag, **kwargs) -> str:
    """Custom a tag processor

    Custom processor for a tag, it removes the entry, because the link
    is already included in the entry.
    """
    return ""


def convert_from_html(html: str) -> str:
    """Convert an HTML string to Markdown

    Convert the html entry to markdown compatible with Discord.
    """
    return html_to_markdown.convert_to_markdown(
        html, custom_converters={"a": process_a_tag}
    )


class DebianDSADataSource(DataSource):
    """Debian Security Advisories data source.

    This data sources retrieves information from Debian Security Advisories
    RSS link for listing latest security announcements.
    """

    def get_entries(self) -> list[Entry]:
        data = feedparser.parse("https://www.debian.org/security/dsa-long.rdf")
        entries = []
        for entry in data.entries:
            entries.append(
                Entry(
                    title=entry.title,
                    link=entry.link,
                    pub_date=entry.updated,
                    content=convert_from_html(entry.summary),
                )
            )
        return entries
