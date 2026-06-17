# 🐍 Python for DevOps — Practice Lab

> A simple **clone-and-go** project to revise the Python you actually use as a DevOps / Platform / SRE engineer: reading logs, crunching data, calling commands, and writing small automation scripts.

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🎯 Why this repo?

When people learn Python they often build to-do apps and games. But on a DevOps job you mostly do four things: **read files and logs, shape data, run commands, and automate boring tasks**. This lab focuses on exactly that.

Everything uses only the **Python standard library** — no `pip install` needed to run the exercises. You practise on real-looking data: a web-server log, a list of employees, and a JSON file of servers with CPU/memory stats.

## 🗺️ Visual overview

A picture before the practice. Full set (light + dark, ready for slides/LinkedIn) is in the [diagram gallery](docs/README.md).

**Anatomy of a DevOps script** — read input → parse/validate → transform → output. Most automation follows this shape.

<picture><source media="(prefers-color-scheme: dark)" srcset="docs/01-script-anatomy-dark.png"><img alt="Anatomy of a DevOps script" src="docs/01-script-anatomy.png"></picture>

**Parsing logs** and **running commands with `subprocess`** — two everyday DevOps tasks.

<picture><source media="(prefers-color-scheme: dark)" srcset="docs/02-log-parsing-dark.png"><img alt="Log parsing pipeline" src="docs/02-log-parsing.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="docs/03-subprocess-dark.png"><img alt="subprocess flow" src="docs/03-subprocess.png"></picture>

## 🗂️ What's inside

```
python-devops-practice-lab/
├── README.md                 ← you are here
├── CHEATSHEET.md             ← 1-page Python-for-DevOps reminder
├── CONTRIBUTING.md           ← how to add your own exercises
├── requirements.txt          ← exercises need nothing; lists optional dev tools
├── generate_data.py          ← creates the sample data in data/
├── data/                     ← sample files used by every exercise
│   ├── access.log
│   ├── employees.csv
│   └── servers.json
├── 01-python-essentials/     ← warm-up: variables, if, loops, functions, files
│   └── README.md
├── 02-parsing-and-data/      ← logs, CSV, JSON (the bread and butter)
│   ├── README.md
│   ├── exercise-1-log-parser.py
│   ├── exercise-2-csv-report.py
│   ├── exercise-3-json-config.py
│   └── solutions/
└── 03-automation/            ← files, subprocess, health checks
    ├── README.md
    ├── exercise-1-file-cleanup.py
    ├── exercise-2-run-commands.py
    ├── exercise-3-health-check.py
    └── solutions/
```

## 🚀 Quick start

```bash
# 1. Get the code
git clone https://github.com/shubhs248/python-devops-practice-lab.git
cd python-devops-practice-lab

# 2. Create the sample data
python generate_data.py

# 3. Open the instructions for each part and start practising
cat 01-python-essentials/README.md
cat 02-parsing-and-data/README.md
cat 03-automation/README.md
```

> 💡 Use `python3` instead of `python` if that is how Python is installed on your machine.
> On **Windows**, `python` usually works in PowerShell.

## 🧭 Suggested path (about 2 hours)

| # | Part | What you practise | Time |
|---|------|-------------------|------|
| 1 | [Python Essentials](01-python-essentials/README.md) | variables, `if`, `for`/`while`, functions, reading files | 30 min |
| 2 | [Parsing & Data](02-parsing-and-data/README.md) | logs, `csv`, `json`, `collections.Counter`, `argparse` | 45 min |
| 3 | [Automation](03-automation/README.md) | `pathlib`, `subprocess`, retries, exit codes, `logging` | 45 min |

## ✅ How each exercise works

1. Read the part's `README.md`. It tells you **the goal** and **which idea you are practising**.
2. Open the `exercise-*.py` file. It has a short brief, hints, and `# TODO` lines showing where to write your code.
3. Write your answer, then run it, for example: `python 02-parsing-and-data/exercise-1-log-parser.py`
4. Stuck? Compare with the ready-made answer in the part's `solutions/` folder.

---

## 🎤 Prepping for an interview?

After you've done the exercises, open **[INTERVIEW-QUESTIONS.md](INTERVIEW-QUESTIONS.md)** — the Python-for-DevOps questions interviewers actually ask, in plain English, with short answers you can say out loud and live-coding prompts to rehearse.

---

## ⭐ Found this useful?

If this lab helped you, here is how you can support it and help others find it:

- **Star** ⭐ the repo so more people discover it.
- **Fork** 🍴 it and practise on your own copy.
- **Share** 🔗 it on LinkedIn and tag me — I would love to see your progress.
- **Contribute** 🤝 a new exercise, dataset, or fix. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 👋 About the author

Made with care by **Shubham Sharma**.

- GitHub: [github.com/shubhs248](https://github.com/shubhs248)
- LinkedIn: [linkedin.com/in/shubhs248](https://www.linkedin.com/in/shubhs248)

## 📜 License

MIT — free to use, fork, teach with, and share. A star ⭐ or a tag on LinkedIn is always appreciated!
