# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

from config import MESSAGE_WAIT_TIME, NOTICES_FETCH_WAIT_TIME


def get_message_wait_time():
    """Get the wait time between sending messages in seconds."""
    return MESSAGE_WAIT_TIME


def get_notices_fetch_wait_time():
    """Get the wait time between fetching notices in seconds."""
    return NOTICES_FETCH_WAIT_TIME
