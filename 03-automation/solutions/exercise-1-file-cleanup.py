#!/usr/bin/env python3
"""Solution — Exercise 3.1 Old Log Cleanup"""
import argparse
import time
from pathlib import Path

LOGS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "logs"


def human_size(num_bytes: int) -> str:
    """Turn a byte count into something readable like 1.2 KB."""
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def main() -> None:
    parser = argparse.ArgumentParser(description="Delete log files older than N days.")
    parser.add_argument("--days", type=int, default=30,
                        help="delete files older than this many days (default 30)")
    parser.add_argument("--dry-run", action="store_true",
                        help="only show what would be deleted")
    args = parser.parse_args()

    if not LOGS_DIR.exists():
        print(f"Folder not found: {LOGS_DIR}")
        print("Run 'python generate_data.py' first to create it.")
        return

    now = time.time()
    deleted_count = 0
    freed_bytes = 0
    mode = "[dry-run] would delete" if args.dry_run else "deleted"

    for path in sorted(LOGS_DIR.glob("*.log")):
        stat = path.stat()
        age_days = (now - stat.st_mtime) / 86400
        size = stat.st_size

        if age_days >= args.days:
            print(f"{mode}: {path.name}  (age {age_days:.0f}d, {human_size(size)})")
            deleted_count += 1
            freed_bytes += size
            if not args.dry_run:
                path.unlink()
        else:
            print(f"keeping:        {path.name}  (age {age_days:.0f}d, {human_size(size)})")

    verb = "would free" if args.dry_run else "freed"
    print("-" * 50)
    print(f"{deleted_count} file(s) older than {args.days} days; {verb} {human_size(freed_bytes)}.")


if __name__ == "__main__":
    main()
