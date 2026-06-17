#!/usr/bin/env python3
"""
Exercise 3.1 — Old Log Cleanup
============================================================================
WHAT YOU PRACTISE: pathlib + file ages + a safe --dry-run option + argparse

WHAT TO BUILD:
    A script that finds log files older than a given number of days inside
    ../data/logs/ and deletes them. This is a very common DevOps job (disks
    fill up with old logs!), so make it SAFE:
      • --days N      delete files older than N days (default 30)
      • --dry-run     only show what WOULD be deleted, do not delete anything

    Always print each file with its age in days and its size, then a summary
    line: how many files were deleted (or would be), and how much space freed.

HOW TO RUN:
    python exercise-1-file-cleanup.py --days 14 --dry-run
    python exercise-1-file-cleanup.py --days 14            # actually deletes

    (Run `python generate_data.py` first to create data/logs/.)

HINTS:
    • Read the options:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("--days", type=int, default=30)
        parser.add_argument("--dry-run", action="store_true")
        args = parser.parse_args()
    • Find files:           for path in LOGS_DIR.glob("*.log"):
    • A file's age in days:
        import time
        age_days = (time.time() - path.stat().st_mtime) / 86400
    • A file's size in bytes:   path.stat().st_size
    • Delete a file:            path.unlink()    (skip this when --dry-run is on)
============================================================================
"""
import argparse
import time
from pathlib import Path

LOGS_DIR = Path(__file__).resolve().parent.parent / "data" / "logs"


def main() -> None:
    # TODO 1: set up argparse with --days (default 30) and --dry-run


    # TODO 2: make sure LOGS_DIR exists; if not, tell the user to run generate_data.py


    # TODO 3: go through every *.log file, work out its age in days and its size


    # TODO 4: if it is older than --days, print it; delete it unless --dry-run is on


    # TODO 5: print a summary (count of files + total size handled)

    # Remove this line once you start writing your solution above:
    print("Not finished yet - complete the # TODO steps in this file.")


if __name__ == "__main__":
    main()
