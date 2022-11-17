import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()


class Storage:
    def __init__(self):
        self.conn = sqlite3.connect(os.getenv("DATABASE"))
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS readings (
                start_time TEXT PRIMARY KEY,
                end_time TEXT,
                usage FLOAT
            )
            """
        )

    def insert_record(self, reading):
        try:
            self.cursor.execute(
                "INSERT INTO readings (start_time, end_time, usage) VALUES (?, ?, ?)",
                (
                    reading["interval_start"],
                    reading["interval_end"],
                    reading["consumption"],
                ),
            )
            return True
        except sqlite3.IntegrityError:
            # ignore duplicate readings
            return False

    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
