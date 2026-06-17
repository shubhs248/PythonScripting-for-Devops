# Part 3 — Automation (Real DevOps Scripts)

## 🎯 Goal
Put it all together and write the kind of small scripts you actually ship: clean up old files, run system commands and read their output, and run a health check that exits with the right code for a pipeline.

## 🧠 What you practise here
- Working with files and folders using `pathlib`
- File ages and sizes (`stat`, `datetime`) and a safe `--dry-run` option
- Running shell commands with `subprocess` and checking the result
- Reading options from the command line with `argparse`
- Retrying something until it works
- Exit codes (`sys.exit`) so other tools know if it passed or failed
- Clean output with the `logging` module

---

## 📝 The 3 exercises

| # | File | What it tests |
|---|------|---------------|
| 1 | `exercise-1-file-cleanup.py`  | `pathlib` + file ages + a safe `--dry-run` flag |
| 2 | `exercise-2-run-commands.py`  | `subprocess` + checking return codes |
| 3 | `exercise-3-health-check.py`  | retries + `logging` + exit codes |

> Run `python generate_data.py` first — it creates the `data/logs/` folder that exercise 1 cleans up.

Each starter file has the brief, the hints, and `# TODO` lines. Write your code, then run it:

```bash
python 03-automation/exercise-1-file-cleanup.py --days 14 --dry-run
python 03-automation/exercise-2-run-commands.py
python 03-automation/exercise-3-health-check.py
```

Ready-made answers are in [`solutions/`](solutions).

🎉 Finished all three parts? You have now revised the Python that DevOps work is built on. Go back to the [main README](../README.md) and share your fork on LinkedIn!

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add an exercise or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
