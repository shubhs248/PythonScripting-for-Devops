#!/usr/bin/env python3
"""Solution — Exercise 3.2 Run System Commands"""
import subprocess


def run(cmd: list[str]) -> tuple[bool, str]:
    """Run a command. Return (success?, output-or-error-text)."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        return False, "command not found"

    if result.returncode == 0:
        # Some tools (like `python --version`) print to stderr — fall back to it.
        output = (result.stdout or result.stderr).strip()
        return True, output

    return False, (result.stderr or result.stdout).strip()


def main() -> None:
    commands = [
        ["python", "--version"],
        ["whoami"],
        ["python", "-c", "print('hello-devops')"],
        ["definitely-not-a-real-cmd"],
    ]

    print("System info report")
    print("=" * 50)
    for cmd in commands:
        ok, output = run(cmd)
        status = "SUCCESS" if ok else "FAILED "
        printable = " ".join(cmd)
        print(f"[{status}] {printable}")
        print(f"          -> {output}")
    print("=" * 50)


if __name__ == "__main__":
    main()
