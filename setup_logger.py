# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import logging
import os
import sys


def configure_logger():
    """
    Configure logging using a file with path assigned from LOG_FILE
    environment variable.
    """
    log_path = os.environ.get("LOG_FILE")
    file_handler = logging.FileHandler(log_path)
    stream_handler = logging.StreamHandler(sys.stderr)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    root = logging.root
    root.addHandler(file_handler)
    root.addHandler(stream_handler)
    root.setLevel(logging.INFO)


configure_logger()
