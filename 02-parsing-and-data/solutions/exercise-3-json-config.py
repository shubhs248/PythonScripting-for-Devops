#!/usr/bin/env python3
"""Solution — Exercise 2.3 JSON Config Reader"""
import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "servers.json"
OUTPUT_PATH = Path(__file__).resolve().parent.parent.parent / "output" / "server_summary.json"


def main() -> None:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = json.load(f)

    servers = config["servers"]
    cpu_limit = config["thresholds"]["cpu_percent"]
    mem_limit = config["thresholds"]["mem_percent"]

    up = sum(1 for s in servers if s["status"] == "up")
    down = sum(1 for s in servers if s["status"] == "down")

    over_threshold = [
        s["name"]
        for s in servers
        if s["cpu"] > cpu_limit or s["mem"] > mem_limit
    ]

    print(f"Environment: {config['environment']}")
    print(f"Servers up:   {up}")
    print(f"Servers down: {down}")
    print(f"Over threshold (cpu>{cpu_limit} or mem>{mem_limit}): {over_threshold or 'none'}")

    summary = {
        "environment": config["environment"],
        "total": len(servers),
        "up": up,
        "down": down,
        "over_threshold": over_threshold,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"\nSaved summary to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
