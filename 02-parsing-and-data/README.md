# Part 2 — Parsing & Data (The Bread and Butter)

*A typical log-parsing pipeline:*

<picture><source media="(prefers-color-scheme: dark)" srcset="../docs/02-log-parsing-dark.png"><img alt="Log parsing pipeline" src="../docs/02-log-parsing.png"></picture>

## 🎯 Goal
Most DevOps Python is about taking messy text or structured files and turning them into useful answers. Here you parse a **log file**, a **CSV**, and a **JSON** config — the three formats you meet most often.

## 🧠 What you practise here
- Reading files safely with `with open(...)`
- Splitting and cleaning text (`split`, `strip`) and using `re` (regex) when needed
- Counting things with `collections.Counter`
- The `csv` module (reading rows as dictionaries)
- The `json` module (loading config, looping over it, writing a report)
- Reading options from the command line with `argparse`
- Handling errors so your script fails with a clear message

---

## 📝 The 3 exercises

| # | File | What it tests |
|---|------|---------------|
| 1 | `exercise-1-log-parser.py`  | reading a log + counting status codes / top IPs |
| 2 | `exercise-2-csv-report.py`  | the `csv` module + grouping & averages by team |
| 3 | `exercise-3-json-config.py` | the `json` module + filtering + writing a report |

Each starter file has the brief, the hints, and `# TODO` lines. Write your code, then run it:

```bash
python 02-parsing-and-data/exercise-1-log-parser.py
python 02-parsing-and-data/exercise-2-csv-report.py
python 02-parsing-and-data/exercise-3-json-config.py
```

Ready-made answers are in [`solutions/`](solutions). Try first, then check.

➡️ Next: [Part 3 — Automation](../03-automation/README.md).

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add an exercise or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
