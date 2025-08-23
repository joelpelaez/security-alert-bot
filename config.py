# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import os

from dotenv import load_dotenv

load_dotenv()

# Define enabled data sources for notices.
DATA_SOURCES = (
    "FreeBSDDataSource",
    "DebianDSADataSource",
)

# Define enabled bots for sending messages. No used for now
BOTS = ("DiscordBot",)

# Define sqlite database file path
DB_PATH = os.getenv("DB_PATH")

# Define wait time between messages from same notice fetch.
MESSAGE_WAIT_TIME = os.environ.get("MESSAGE_WAIT_TIME", 10)

# Define wait time between notices fetch to sources.
NOTICES_FETCH_WAIT_TIME = os.environ.get("NOTICES_FETCH_WAIT_TIME", 600)
