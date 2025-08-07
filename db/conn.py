# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import sqlite3

from settings import get_database_location

global_conn = None


def get_connection():
    global global_conn

    if global_conn is None:
        db_file = get_database_location()
        global_conn = sqlite3.connect(db_file, autocommit=False)

    return global_conn
