# 🤝 Contributing

Thanks for thinking about helping out! This is a learning project, so contributions of every size are welcome — even fixing a typo.

If this repo helped you, the easiest way to support it is to **star** ⭐ it, **fork** 🍴 it, and **share** 🔗 it on LinkedIn so others can find it too.

## Ways you can help

- **Fix something** — a typo, a broken link, or code that does not run.
- **Add a new exercise** — more practice on parsing, automation, APIs, testing, etc.
- **Add a new dataset** — another realistic file people can practise on.
- **Improve the wording** — make an explanation clearer or simpler.
- **Keep it standard-library-only** where you can, so people can run it with no setup.

## How to contribute (step by step)

1. **Fork** this repo to your own GitHub account (use the "Fork" button at the top).
2. **Clone** your fork to your computer:
   ```bash
   git clone https://github.com/<your-username>/python-devops-practice-lab.git
   cd python-devops-practice-lab
   ```
3. **Create a branch** for your change:
   ```bash
   git checkout -b add-api-exercise
   ```
4. **Make your change** and test it (see the checklist below).
5. **Commit** with a short, clear message:
   ```bash
   git add .
   git commit -m "Add a parsing exercise on YAML configs"
   ```
6. **Push** your branch and open a **Pull Request**:
   ```bash
   git push -u origin add-api-exercise
   ```
   Then open the PR on GitHub and describe what you changed.

## Adding a new exercise

Please keep the same simple style so the repo stays easy to follow:

- Put the **starter** script in the right part folder (for example `03-automation/`).
- Put the matching **answer** in that part's `solutions/` folder, using the same file name.
- At the top of the starter script, add a docstring (`""" ... """`) with:
  - **WHAT YOU PRACTISE** — the idea in one line.
  - **WHAT TO BUILD** — what the script should do.
  - **HOW TO RUN** — an example command.
  - **HINTS** — a few helpful tips.
- Use `# TODO` lines to show where the learner should write code.

## Checklist before you open a PR

- [ ] The script runs without errors: `python your-script.py`.
- [ ] It uses only the standard library (or you explained the extra package in the PR).
- [ ] Comments and instructions use plain, simple English.
- [ ] (Nice to have) It passes the linter: `ruff check .`
- [ ] If you added a new part, you linked it from the main `README.md`.

## Code of conduct

Be kind and helpful. This is a place for people to learn, so assume good intent and keep feedback friendly.

---

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
