#!/usr/bin/env python3
"""Solution — Exercise 3.3 Server Health Check"""
import json
import logging
import sys
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "servers.json"

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("healthcheck")


def is_healthy(server: dict, cpu_limit: int, mem_limit: int) -> bool:
    return (
        server["status"] == "up"
        and server["cpu"] < cpu_limit
        and server["mem"] < mem_limit
    )


def main() -> None:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = json.load(f)

    cpu_limit = config["thresholds"]["cpu_percent"]
    mem_limit = config["thresholds"]["mem_percent"]

    healthy = 0
    unhealthy = 0

    for server in config["servers"]:
        name = server["name"]
        if is_healthy(server, cpu_limit, mem_limit):
            healthy += 1
            log.info("%s is healthy (cpu=%s%% mem=%s%%)", name, server["cpu"], server["mem"])
        else:
            unhealthy += 1
            reason = "down" if server["status"] != "up" else "over threshold"
            log.warning("%s is UNHEALTHY (%s, cpu=%s%% mem=%s%%)",
                        name, reason, server["cpu"], server["mem"])

    print("-" * 50)
    print(f"Healthy: {healthy}   Unhealthy: {unhealthy}")

    if unhealthy > 0:
        print("Result: FAIL")
        sys.exit(1)
    print("Result: OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
