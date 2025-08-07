# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

from .manager import Manager
from model.entry import Entry


class Bot:
    """
    Basic abstraction for all Bot implementations.
    It helps to message dispatcher to send to multiple bot implementations.
    """

    def register_manager(self, manager: Manager) -> None:
        """Register the manager to start when the bot is ready"""
        pass

    async def start_async(self):
        """
        Starts the bot.
        """
        pass

    async def send_formatted_message(self, entry: Entry):
        """
        Send a formatted message using the bot with an Entry object
        for making a bot specific formatted message.
        """
        pass

    async def send_message(self, message):
        """
        Send a plain text message using the boot.
        """
        pass
