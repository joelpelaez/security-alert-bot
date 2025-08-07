# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.


def patch_getaddrinfo():
    """
    This function helps to patch getaddrinfo to avoid use IPv6 addresses.
    It can help when IPv6 host address are available but exists issues with
    connectivity.
    """

    import socket

    # Copy original getaddrinfo
    original_getaddrinfo = socket.getaddrinfo

    # Call to original function always as AF_INET
    def getaddrinfo_ipv4_only(host, port, family=0, type=0, proto=0, flags=0):
        # Force family to AF_INET (IPv4)
        return original_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)

    # Reassign new getaddrinfo function
    socket.getaddrinfo = getaddrinfo_ipv4_only
