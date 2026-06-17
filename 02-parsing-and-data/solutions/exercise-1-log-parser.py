#!/usr/bin/env python3
"""Solution — Exercise 2.1 Log Parser"""
from collections import Counter
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "access.log"


def main() -> None:
    status_counts: Counter = Counter()
    ip_counts: Counter = Counter()
    total = 0

    with open(LOG_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            # A valid line has the IP first and the status code as the 9th item.
            if len(parts) < 9:
                continue
            ip = parts[0]
            status = parts[8]
            ip_counts[ip] += 1
            status_counts[status] += 1
            total += 1

    print(f"Total requests: {total}\n")

    print("Requests by status code:")
    for code, count in sorted(status_counts.items()):
        print(f"  {code}: {count}")

    print("\nTop 3 IP addresses:")
    for ip, count in ip_counts.most_common(3):
        print(f"  {ip}: {count} request(s)")


if __name__ == "__main__":
    main()
