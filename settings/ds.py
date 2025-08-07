# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import ds
from domain import DataSource

from config import DATA_SOURCES


def get_data_sources() -> list[type[DataSource]]:
    """Get enabled data sources for notices fetching

    Get enabled data sources defined in settings.base module. This function
    does not return instantiated classes (objects).

    Returns:
        list[type[DataSource]]: Enabled data sources classes (types)
    """
    modules = [getattr(ds, ds_class) for ds_class in DATA_SOURCES]
    return modules
