#!/usr/bin/env python3
"""
Exercise 3.3 — Server Health Check
============================================================================
WHAT YOU PRACTISE: looping over data + retries + logging + exit codes

WHAT TO BUILD:
    Read ../data/servers.json and check each server's health. For every server:
      • it is HEALTHY if status == "up" AND cpu < cpu_limit AND mem < mem_limit
        (the limits come from the "thresholds" section of the JSON)
      • otherwise it is UNHEALTHY

    Use the `logging` module (not print) so the output looks like a real tool:
      • log healthy servers at INFO level
      • log unhealthy servers at WARNING level

    At the end, print how many were healthy / unhealthy, and:
      • exit with code 0 if everything is healthy
      • exit with code 1 if anything is unhealthy
        (this is what lets a CI/CD pipeline or cron job know it failed)

    BONUS (retry pattern): wrap the "down" check in a retry helper that tries
    up to 3 times before giving up — handy when a check is flaky.

HOW TO RUN:
    python exercise-3-health-check.py
    echo $?      # see the exit code (Linux/macOS).  On PowerShell: echo $LASTEXITCODE

HINTS:
    • Set up logging once at the top:
        import logging
        logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
        log = logging.getLogger("healthcheck")
        log.info("..."); log.warning("...")
    • Load the JSON like in exercise 2.3 (json.load).
    • Exit with a code:   import sys; sys.exit(1)
============================================================================
"""
import json
import logging
import sys
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "data" / "servers.json"

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("healthcheck")


def is_healthy(server: dict, cpu_limit: int, mem_limit: int) -> bool:
    # TODO 1: return True only when the server is "up" and under both limits
    raise NotImplementedError("Implement is_healthy() — see the brief above.")


def main() -> None:
    # TODO 2: load the JSON config and read the cpu/mem limits from thresholds


    # TODO 3: loop over the servers; log healthy ones at INFO, unhealthy at WARNING,
    #         and count how many of each there are


    # TODO 4: print the summary and exit with code 0 (all healthy) or 1 (any unhealthy)

    # Remove this line once you start writing your solution above:
    print("Not finished yet - complete the # TODO steps in this file.")


if __name__ == "__main__":
    main()
