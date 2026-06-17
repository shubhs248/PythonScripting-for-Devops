# Part 1 — Python Essentials for DevOps (Warm-up)

*The anatomy of a typical DevOps script:*

<picture><source media="(prefers-color-scheme: dark)" srcset="../docs/01-script-anatomy-dark.png"><img alt="Anatomy of a DevOps script" src="../docs/01-script-anatomy.png"></picture>

## 🎯 Goal
Refresh the basic Python you will use again and again in DevOps scripts, before you move on to the real tasks in parts 2 and 3.

## 🧠 What you practise here
| Idea | What it is for |
|------|----------------|
| variables & f-strings | Hold values and build nice messages |
| `if` / `elif` / `else` | Make decisions |
| `for` / `while` loops | Repeat work, go through lists and files |
| functions | Reuse a block of code, give it a name |
| lists & dictionaries | Store many values; store key → value pairs |
| reading files | Open a file and go through it line by line |
| `sys.argv` / `argparse` | Read the values someone types after the script name |

You do not need any extra packages — everything here is built into Python.

---

## 📝 Tasks
Open a Python file (or the `python` shell) and try each one. Have a go **before** you read the answer. The answers are at the bottom.

> Run `python generate_data.py` first so the `data/` folder is ready.

1. **Print a message.** Make a variable `name = "web-01"` and print `Checking server: web-01` using an f-string.
2. **Decide.** Given `cpu = 90`, print `HIGH` if cpu is 80 or more, else print `OK`.
3. **Count with a loop.** Print the numbers 1 to 5, each on its own line.
4. **Sum a list.** Given `sizes = [120, 340, 90, 510]`, add them up and print the total.
5. **Go through a dictionary.** Given `server = {"name": "db-01", "cpu": 55, "mem": 88}`, print each key and value as `key = value`.
6. **Write a function.** Write `is_healthy(cpu, mem)` that returns `True` only when cpu < 80 **and** mem < 85. Test it with a few values.
7. **Read a file.** Open `data/access.log` and print how many lines it has.
8. **Filter while reading.** Print only the lines in `data/access.log` that contain `500`.
9. **List comprehension.** From `nums = [4, 7, 10, 15, 20]`, build a new list with only the even numbers.
10. **Read an argument.** Make a script that prints the first value typed after its name, or a friendly message if nothing was typed.

---

## ✅ Answers

```python
# 1. Print a message
name = "web-01"
print(f"Checking server: {name}")

# 2. Decide
cpu = 90
if cpu >= 80:
    print("HIGH")
else:
    print("OK")

# 3. Count with a loop
for i in range(1, 6):
    print(i)

# 4. Sum a list
sizes = [120, 340, 90, 510]
print(sum(sizes))           # or loop and add: total = 0; for s in sizes: total += s

# 5. Go through a dictionary
server = {"name": "db-01", "cpu": 55, "mem": 88}
for key, value in server.items():
    print(f"{key} = {value}")

# 6. Write a function
def is_healthy(cpu, mem):
    return cpu < 80 and mem < 85

print(is_healthy(35, 60))   # True
print(is_healthy(90, 60))   # False

# 7. Read a file (count lines)
with open("data/access.log", encoding="utf-8") as f:
    lines = f.readlines()
print(len(lines))

# 8. Filter while reading
with open("data/access.log", encoding="utf-8") as f:
    for line in f:
        if "500" in line:
            print(line.strip())

# 9. List comprehension
nums = [4, 7, 10, 15, 20]
evens = [n for n in nums if n % 2 == 0]
print(evens)

# 10. Read an argument
import sys
if len(sys.argv) > 1:
    print(f"You typed: {sys.argv[1]}")
else:
    print("Please type a value after the script name.")
```

➡️ When you are comfortable, move on to [Part 2 — Parsing & Data](../02-parsing-and-data/README.md).

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add a task or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
