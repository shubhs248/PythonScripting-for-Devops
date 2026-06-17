#!/usr/bin/env python3
"""
Exercise 2.1 — Log Parser
============================================================================
WHAT YOU PRACTISE: reading a file + splitting text + counting with a dict

WHAT TO BUILD:
    Read ../data/access.log and print a small report:
      • the total number of requests (lines)
      • how many requests there were for each status code (200, 404, 500, ...)
      • the top 3 IP addresses that made the most requests

    Each log line looks like this (the IP is the FIRST item, and the status
    code is the 9th item when you split on spaces):

        192.168.1.10 - - [17/Jun/2026:09:01:12 +0530] "GET /index.html HTTP/1.1" 200 1024

HOW TO RUN:
    python exercise-1-log-parser.py

HINTS:
    • Build the path safely:
        from pathlib import Path
        log_path = Path(__file__).resolve().parent.parent / "data" / "access.log"
    • Split a line into items:   parts = line.split()
        parts[0] is the IP, parts[8] is the status code.
    • Counting is easiest with Counter:
        from collections import Counter
        status_counts = Counter()
        status_counts[code] += 1
    • Top 3 of a Counter:        counter.most_common(3)
============================================================================
"""
from collections import Counter
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent.parent / "data" / "access.log"


def main() -> None:
    status_counts: Counter = Counter()
    ip_counts: Counter = Counter()
    total = 0

    # TODO 1: open LOG_PATH and go through it one line at a time


    # TODO 2: for each line, split it, count the status code and the IP,
    #         and add 1 to total


    # TODO 3: print the total number of requests


    # TODO 4: print the count for each status code


    # TODO 5: print the top 3 IP addresses (use most_common)

    # Remove this line once you start writing your solution above:
    print("Not finished yet - complete the # TODO steps in this file.")


if __name__ == "__main__":
    main()
