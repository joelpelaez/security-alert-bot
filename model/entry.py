# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Entry:
    """Define model for notice entries

    This model allows to generalize notices using a standard structure and
    reuse it for multiple bot implementations.

    Attributes:
        title (str):
          The title of the notice, it must be plain text and be unique between all
          data sources.
        content (str):
          The content of the notice, it can be plain text or bot-compatible markdown.
        link (str):
          The link of the notice, it must be a valid URL.
        pub_date (datetime):
          The date the notice was published, used for reference.
    """

    title: str
    content: str
    link: str
    pub_date: datetime
