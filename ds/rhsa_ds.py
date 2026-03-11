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

from domain.datasource import DataSource
from model.entry import Entry


class RedHatSecurityErrataDataSource(DataSource):
    """Red Hat Security Errata data source.

    This data sources retrieves information from Red Hat Security Errata (RHSA)
    RSS link for listing latest security announcements.
    """

    def get_entries(self) -> list[Entry]:
        data = feedparser.parse(
            "https://security.access.redhat.com/data/meta/v1/rhsa.rss"
        )
        entries = []
        for entry in data.entries:
            entries.append(
                Entry(
                    title=entry.title,
                    link=entry.link,
                    pub_date=entry.updated,
                    content=entry.summary,
                )
            )
        return entries
