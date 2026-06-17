#!/usr/bin/env python3
"""
Exercise 2.3 — JSON Config Reader
============================================================================
WHAT YOU PRACTISE: the json module + filtering a list + writing a report

WHAT TO BUILD:
    Read ../data/servers.json (a config file describing servers) and:
      • print how many servers are "up" and how many are "down"
      • print the names of any servers that are OVER a usage threshold
        (cpu above thresholds.cpu_percent OR mem above thresholds.mem_percent)
      • save a short summary to output/server_summary.json

    The file looks like:
        {
          "environment": "staging",
          "thresholds": { "cpu_percent": 80, "mem_percent": 85 },
          "servers": [ { "name": "web-01", "status": "up", "cpu": 35, "mem": 60, ... }, ... ]
        }

HOW TO RUN:
    python exercise-3-json-config.py

HINTS:
    • Load JSON into Python:
        import json
        with open(path, encoding="utf-8") as f:
            config = json.load(f)        # config is now a dict
      Then config["servers"] is a list of dicts, config["thresholds"] is a dict.
    • Count "up" servers:   sum(1 for s in servers if s["status"] == "up")
    • Make the output folder:  Path("output").mkdir(exist_ok=True)
    • Write JSON nicely:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
============================================================================
"""
import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "data" / "servers.json"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "output" / "server_summary.json"


def main() -> None:
    # TODO 1: load the JSON config from CONFIG_PATH


    # TODO 2: count how many servers are "up" and how many are "down"


    # TODO 3: find servers over the cpu OR mem threshold, and print their names


    # TODO 4: build a summary dict and write it to OUTPUT_PATH as JSON
    #         (remember to create the output/ folder first)

    # Remove this line once you start writing your solution above:
    print("Not finished yet - complete the # TODO steps in this file.")


if __name__ == "__main__":
    main()
