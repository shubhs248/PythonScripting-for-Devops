# 🎤 Python for DevOps — Interview Questions

> The Python questions that come up in DevOps / SRE / platform interviews, in plain English with short answers you can say out loud. Do the exercises first, then use this to **explain** your thinking.

**How to use this file:** cover the answers, read a question, answer out loud, then check. Bonus: tie each answer back to an exercise you actually solved in this lab.

---

## 🟢 Warm-up

**1. Why use Python for DevOps instead of bash?**
Bash is great for short glue between commands. Python wins when you need real data structures, parsing (JSON/YAML/CSV), error handling, HTTP calls, testing, or anything more than ~30 lines. It's also cross-platform and easier to read/maintain.

**2. What is the difference between a list, a tuple, a set, and a dict?**
- **list** — ordered, changeable: `[1, 2, 3]`
- **tuple** — ordered, *not* changeable: `(1, 2)`
- **set** — unordered, unique items: `{1, 2}` (great for de-duping)
- **dict** — key→value pairs: `{"host": "web1"}`

**3. How do you read a file safely?**
```python
with open("file.txt") as f:
    for line in f:
        process(line)
```
The `with` block auto-closes the file even if an error happens.

**4. What does `if __name__ == "__main__":` do?**
It runs the code below it only when the file is executed directly, not when it's imported as a module. It's how you make a file both a script and a reusable library.

**5. List comprehension — what and why?**
A short way to build a list: `[x*2 for x in nums if x > 0]`. It's more readable and faster than an equivalent `for` loop with `.append()`.

---

## 🔵 Parsing & data (the bread and butter)

**6. How do you parse a log line and pull out fields?**
Split on a delimiter (`line.split()`), or use a regex (`re.search`) when the format is messier. For structured logs, prefer JSON logging so you can `json.loads()` each line.

**7. How do you count occurrences (e.g. status codes in a log)?**
```python
from collections import Counter
counts = Counter(status_codes)
counts.most_common(5)   # top 5
```
`Counter` is the idiomatic answer and interviewers like seeing it.

**8. How do you read and write CSV?**
Use the `csv` module. `csv.DictReader` gives you each row as a dict keyed by the header — much cleaner than manual splitting, and it handles quoted commas correctly.

**9. JSON: `load` vs `loads` vs `dump` vs `dumps`?**
- `load`/`dump` work with a **file object**.
- `loads`/`dumps` work with a **string** (the `s` = string).
So `json.loads(text)` parses a string, `json.dump(obj, f)` writes to a file.

**10. How do you handle a key that might be missing in a dict?**
Use `.get("key", default)` instead of `dict["key"]` to avoid a `KeyError`, or use `try/except KeyError` when the absence is truly exceptional.

---

## 🟣 Automation & the system

**11. How do you run a shell command from Python?**
```python
import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout, result.returncode)
```
Pass a **list** of args (not a string) and avoid `shell=True` unless you must — it's a security risk with untrusted input.

**12. Why avoid `shell=True`?**
It runs your command through the shell, so untrusted input can inject extra commands (`; rm -rf /`). Passing an args list avoids the shell entirely.

**13. How do you work with files and paths in a cross-platform way?**
Use `pathlib`: `Path("logs") / "app.log"`. It handles Windows vs Linux separators and gives you `.exists()`, `.glob()`, `.stat().st_mtime`, etc.

**14. How would you delete log files older than 7 days?**
Loop over `Path("logs").glob("*.log")`, compare `file.stat().st_mtime` to `time.time() - 7*86400`, and `file.unlink()` the old ones. (That's exactly the file-cleanup exercise in this lab.)

**15. How do you parse command-line arguments?**
Use `argparse`. It gives you `--flags`, defaults, type conversion, help text, and validation for free — far better than reading `sys.argv` by hand.

---

## 🟠 Errors, logging, exit codes

**16. How do you handle errors properly?**
Catch *specific* exceptions (`except FileNotFoundError:`), not a bare `except:`. Do the smallest thing that can fail inside the `try`. Use `finally` or a `with` block for cleanup.

**17. Why use `logging` instead of `print`?**
`logging` gives you levels (DEBUG/INFO/WARNING/ERROR), timestamps, and the ability to route output to files or systems — all configurable without changing the code. `print` is fine for tiny scripts but doesn't scale.

**18. How does a script signal success or failure to the caller (e.g. CI)?**
With its **exit code**: `sys.exit(0)` for success, `sys.exit(1)` (or any non-zero) for failure. CI/CD and other scripts check this to decide whether to continue.

**19. What's the difference between an exception and an exit code?**
An exception is an in-program error you can catch and handle. An exit code is the number the *process* returns to the OS/shell when it finishes. Uncaught exceptions usually result in a non-zero exit code.

---

## 🔴 "Senior" / real-world

**20. What is a virtual environment and why does it matter?**
A venv (`python -m venv .venv`) isolates a project's dependencies so they don't clash with other projects or the system Python. You pin versions in `requirements.txt` so the same versions install everywhere.

**21. How do you make an HTTP request / call an API?**
The `requests` library is the standard: `requests.get(url, timeout=5)`. Always set a **timeout**, check `response.status_code` / `raise_for_status()`, and handle network errors.

**22. How do you make a script idempotent?**
Make it safe to run multiple times with the same result — check before you create, use "create if not exists", and avoid blindly appending. Important for automation that might re-run.

**23. How would you test a DevOps script?**
Split logic into small functions, then unit-test them with `pytest`. Mock external calls (subprocess, HTTP, filesystem) so tests are fast and don't touch real systems.

**24. Your script is slow processing a huge log file. What do you do?**
Stream it line by line (don't `read()` the whole file into memory), use generators, compile regexes once outside the loop, and use `Counter`/dicts instead of repeated list scans. Profile with `cProfile` if unsure.

**25. Generators vs lists — when and why?**
A list holds everything in memory at once. A generator (`yield`, or `(x for x in ...)`) produces items one at a time — essential for large files/streams where you can't fit it all in memory.

---

## 🧠 Whiteboard / live-coding prompts

Try these in this lab before an interview.

1. **Count log lines per status code and print the top 3.** → `Counter` + `most_common(3)`.
2. **Read a CSV and print the average salary per department.** → `DictReader` + a dict of running totals.
3. **Find and delete files older than N days.** → `pathlib.glob` + `st_mtime`.
4. **Call a URL and exit non-zero if it's not HTTP 200.** → `requests.get` + `sys.exit`.
5. **Flatten a nested JSON config and print all keys.** → recursion over dicts/lists.

---

## ⭐ Found this useful?
If this helped your prep, please **star** ⭐, **fork** 🍴, and **share** 🔗 the repo on LinkedIn. Hit a Python question in a real interview? Add it via [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
