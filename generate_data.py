#!/usr/bin/env python3
"""
generate_data.py — prepares the practice lab data.

What it does:
  • Makes sure the data/ folder exists with the sample files
    (access.log, employees.csv, servers.json are already in the repo).
  • Creates a small throwaway folder data/logs/ with a few log files.
    Some are given OLD timestamps and some NEW ones, so the file-cleanup
    exercise in part 3 has realistic files to work with.

Run it with:
    python generate_data.py
"""
from __future__ import annotations

import os
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
LOGS = DATA / "logs"


def make_log_playground() -> None:
    """Create data/logs/ with files of different ages."""
    LOGS.mkdir(parents=True, exist_ok=True)

    # (filename, how many days old, size in lines)
    sample_files = [
        ("app-2026-06-17.log", 0, 50),    # today
        ("app-2026-06-16.log", 1, 40),    # yesterday
        ("app-2026-06-10.log", 7, 30),    # a week ago
        ("app-2026-05-18.log", 30, 20),   # a month ago
        ("app-2026-03-19.log", 90, 10),   # three months ago
        ("debug.log", 45, 5),
        ("error.log", 2, 8),
    ]

    now = time.time()
    one_day = 86400

    for name, days_old, lines in sample_files:
        path = LOGS / name
        with path.open("w", encoding="utf-8") as fh:
            for i in range(lines):
                fh.write(f"{name} line {i + 1}: sample log entry\n")

        # Backdate the file's "modified time" so age-based cleanup is testable.
        old_time = now - (days_old * one_day)
        os.utime(path, (old_time, old_time))

    print(f"==> Created {len(sample_files)} files in {LOGS.relative_to(ROOT)}/")


def main() -> None:
    print("==> Python for DevOps Practice Lab - data setup")
    DATA.mkdir(exist_ok=True)

    expected = ["access.log", "employees.csv", "servers.json"]
    missing = [f for f in expected if not (DATA / f).exists()]
    if missing:
        print(f"    NOTE: these sample files are missing from data/: {missing}")
        print("    Re-clone the repo to get them back.")
    else:
        print(f"    Found sample files: {', '.join(expected)}")

    make_log_playground()

    print()
    print("Setup complete. Start with:")
    print("    python 01-python-essentials/README.md   # (just read this file)")
    print("    python 02-parsing-and-data/exercise-1-log-parser.py")


if __name__ == "__main__":
    main()
