# 📋 Python for DevOps — Quick-Revision Cheatsheet

A one-page reminder of the Python you reach for most in DevOps. Use it alongside the exercises.

## Script skeleton
```python
#!/usr/bin/env python3
"""What this script does, in one line."""

def main():
    ...

if __name__ == "__main__":   # only runs when you start THIS file directly
    main()
```

## Variables, f-strings, conditionals
```python
name = "web-01"
cpu = 90
print(f"{name}: cpu={cpu}%")          # f-string builds text from values

if cpu >= 80:
    print("HIGH")
elif cpu >= 50:
    print("MEDIUM")
else:
    print("OK")
```

## Loops
```python
for i in range(1, 4):        # 1, 2, 3
    print(i)

for item in ["a", "b"]:      # go through a list
    print(item)

for key, value in {"a": 1}.items():   # go through a dict
    print(key, value)

n = 0
while n < 3:                 # keep going while the test is true
    n += 1

# break = stop the loop early   |   continue = skip to the next round
```

## Lists & dictionaries
```python
items = [1, 2, 3]
items.append(4)
evens = [x for x in items if x % 2 == 0]   # list comprehension

server = {"name": "db-01", "cpu": 55}
server["mem"] = 88            # add/update a key
server.get("port", 5432)      # read with a default if missing
```

## Functions
```python
def is_healthy(cpu, mem):
    return cpu < 80 and mem < 85   # and / or / not for combining checks
```

## Reading & writing files
```python
from pathlib import Path
path = Path("data/access.log")

with open(path, encoding="utf-8") as f:   # 'with' closes the file for you
    for line in f:
        print(line.strip())               # strip() removes the newline

with open("output/report.txt", "w", encoding="utf-8") as f:
    f.write("done\n")
```

## CSV and JSON (the two you use most)
```python
import csv, json

with open("data/employees.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):     # each row is a dict keyed by column name
        print(row["name"], int(row["salary"]))

with open("data/servers.json", encoding="utf-8") as f:
    config = json.load(f)             # JSON -> Python dict/list
json.dumps(config, indent=2)          # Python -> pretty JSON text
```

## Counting things
```python
from collections import Counter
c = Counter()
c["200"] += 1
c.most_common(3)                      # the 3 most common items
```

## Command-line options (argparse)
```python
import argparse
p = argparse.ArgumentParser()
p.add_argument("--days", type=int, default=30)
p.add_argument("--dry-run", action="store_true")   # a true/false flag
args = p.parse_args()
print(args.days, args.dry_run)
```

## Running shell commands (subprocess)
```python
import subprocess
r = subprocess.run(["python", "--version"], capture_output=True, text=True)
r.returncode    # 0 means success
r.stdout        # what it printed
```

## Files & folders (pathlib)
```python
from pathlib import Path
p = Path("data/logs")
p.mkdir(parents=True, exist_ok=True)  # make the folder (ok if it exists)
for f in p.glob("*.log"):             # find matching files
    f.stat().st_size                  # size in bytes
    f.unlink()                        # delete the file
```

## Logging & exit codes
```python
import logging, sys
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("app")
log.info("all good"); log.warning("uh oh")

sys.exit(0)     # 0 = success, anything else = failure (pipelines check this)
```

## Handling errors
```python
try:
    value = int("not-a-number")
except ValueError as e:
    print(f"bad input: {e}")
```

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to improve it? See [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
