"""Simple logging: add a line with the time to toolkit.log."""

import time

LOG_FILE = "toolkit.log"


def log(message):
    """Write one line to the log file. Do nothing if the file can't be opened."""
    try:
        file = open(LOG_FILE, "a")
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(now + "  " + message + "\n")
        file.close()
    except OSError:
        pass
