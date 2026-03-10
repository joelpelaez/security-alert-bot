# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) 2026 Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.


class Manager:
    """
    Define a service manager for all interactions between the bots and the data sources.
    It must handle synchronization and race conditions between bot activation and data
    retrival.
    """

    def on_ready(self):
        """
        Called when the bot is ready for send and receive messages.
        """
        pass

    def on_terminate(self):
        """
        Called when the bot has terminated.
        """
        pass

    async def start_async(self):
        """
        Async main loop for the manager, must be called on an async context.
        """
        pass

    async def lock(self):
        """
        Allow to lock the manager waiting for the related bot to become ready.

        The bot must call `on_ready()` for release the lock and start the manager's
        main loop.

        See also:
            `on_ready`
            `start_async`
        """
        pass
