#!/usr/bin/env python3
"""
Exercise 3.2 — Run System Commands
============================================================================
WHAT YOU PRACTISE: subprocess + checking return codes

WHAT TO BUILD:
    A tiny "system info" collector that runs a few shell commands, captures
    their output, and prints a clean report. For each command, show whether it
    SUCCEEDED or FAILED based on its return code (0 = success).

    Run these commands (they work the same on Windows, macOS and Linux):
      • python --version                    (the Python version)
      • whoami                               (the current user)
      • python -c "print('hello-devops')"   (prints text; should always succeed)

    Then run ONE command that does NOT exist, e.g. "definitely-not-a-real-cmd",
    and show that your script handles the failure gracefully instead of crashing.

    NOTE: `echo` is tempting, but on Windows it is a shell built-in, not a real
    program, so subprocess cannot run it directly. That is why we use
    `python -c ...` instead — it behaves the same everywhere.

HOW TO RUN:
    python exercise-2-run-commands.py

HINTS:
    • Run a command and capture its output:
        import subprocess
        result = subprocess.run(
            ["python", "--version"],
            capture_output=True, text=True
        )
        result.returncode   # 0 means success
        result.stdout       # what it printed
        result.stderr       # any error text
    • A command that does not exist raises FileNotFoundError — wrap the call
      in try/except so your script keeps going.
    • Build a small helper function run(cmd) that returns (ok, output) so you
      do not repeat yourself.
============================================================================
"""
import subprocess


def run(cmd: list[str]) -> tuple[bool, str]:
    """Run a command. Return (success?, output-or-error-text)."""
    # TODO 1: run the command with subprocess.run(capture_output=True, text=True)
    #         return (True, stdout) when returncode is 0, else (False, stderr)
    #         catch FileNotFoundError and return (False, "command not found")
    raise NotImplementedError("Implement run() — see the hints above.")


def main() -> None:
    commands = [
        ["python", "--version"],
        ["whoami"],
        ["python", "-c", "print('hello-devops')"],
        ["definitely-not-a-real-cmd"],
    ]

    # TODO 2: run each command with your run() helper


    # TODO 3: print each command, whether it SUCCEEDED or FAILED, and its output

    # Remove this line once you start writing your solution above:
    print("Not finished yet - complete the # TODO steps in this file.")


if __name__ == "__main__":
    main()
