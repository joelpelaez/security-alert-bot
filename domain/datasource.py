# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) 2026 Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

from aiohttp import ClientSession

from model.entry import Entry


class DataSource:
    """Define a generic interface for notices data sources

    This class helps to create a generic interface for extract notices
    for multiple data sources and retrieving it in a specific structure.
    """

    async def get_entries(self, session: ClientSession) -> list[Entry]:
        """Get all notices entries available from the data source

        This method obtains the available entries from the data source,
        it can change between calls, because some sources only publishes the
        latest entries. It can requires handle message following using
        other mechanisms as store it in a database.

        Returns:
            list[Entry]: list of entries available in the data source
        """
        pass
