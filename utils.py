# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) 2026 Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import time
from datetime import datetime


def struct_time_to_datetime(struct_time):
    """Convert a struct_time object to a datetime object.

    This function allows use FeedParserDict parsed datetime on struct_time
    format and convert to a datetime object for allow filtering and sorting.
    """
    return datetime.fromtimestamp(time.mktime(struct_time))
