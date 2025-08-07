# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import bot
from domain.bot import Bot

from config import BOTS


def get_bots() -> list[type[Bot]]:
    """Get enabled bots

    This function retrieves enabled bots from settings, as class values
    (there are not instanced in this point).

    Returns:
        list[type[Bot]]: Enabled bots classes (types)
    """
    modules = [getattr(bot, bot_class) for bot_class in BOTS]
    return modules
