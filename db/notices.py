# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

from sqlite3 import Connection

from ds import Entry


class Notices:
    """
    Define the table operations for notices.

    The table name is 'announce'.
    """

    def __init__(self, conn: Connection):
        """
        Create a new notices table manager from a database connection.
        """
        self.conn: Connection = conn

    def _check_exist(self):
        """
        Check if the notices table exists.
        """
        cursor = self.conn.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'notices';
        """)

        self.conn.commit()

        rows = cursor.fetchall()

        return len(rows) > 0

    def _create_table(self):
        """
        Create the notices table if it doesn't exist. Also create the necessary
        indices.
        """
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS announce (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                title       VARCHAR(80) NOT NULL,
                link        VARCHAR(200) NOT NULL,
                pub_date    DATETIME NOT NULL,
                content     TEXT NULL
            );
        """)

        self.conn.execute("""
            CREATE INDEX IF NOT EXISTS announce_title_idx ON announce(title);
        """)

        self.conn.commit()

    def prepare_announce_table(self):
        if not self._check_exist():
            self._create_table()

    def add_announce(self, entry: Entry):
        cursor = self.conn.execute(
            """
            INSERT INTO announce (title, link, pub_date, content)
            VALUES (?, ?, ?, ?);
            """,
            [entry.title, entry.link, entry.pub_date, entry.content],
        )

        self.conn.commit()

        return cursor.lastrowid > 0

    def exists_announce(self, entry: Entry) -> bool:
        cursor = self.conn.execute(
            """
            SELECT COUNT(*) FROM announce WHERE title = ?;
            """,
            [entry.title],
        )

        self.conn.commit()

        (count,) = cursor.fetchone()

        return count > 0
