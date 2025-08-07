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

from config import DB_PATH


def get_database_location():
    """Get the path to the database.

    Returns:
        str: Path to the database.
    """
    path = DB_PATH
    if path is not None:
        return path

    default_dirpath = os.path.expanduser("~/.sec-alert-bot")
    if not os.path.exists(default_dirpath):
        os.mkdir(default_dirpath)

    default_dbpath = os.path.join(default_dirpath, "db.sqlite")
    return default_dbpath
