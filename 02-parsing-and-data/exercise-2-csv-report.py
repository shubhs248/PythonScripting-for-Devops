#!/usr/bin/env python3
"""
Exercise 2.2 — CSV Report
============================================================================
WHAT YOU PRACTISE: the csv module + grouping data + averages

WHAT TO BUILD:
    Read ../data/employees.csv and print a report grouped by department:
      • for each department: the number of people, and the average salary
      • at the end: the name of the highest-paid person overall

    The CSV has these columns:  id, name, department, salary, age

HOW TO RUN:
    python exercise-2-csv-report.py

HINTS:
    • Read rows as dictionaries so you can use column names:
        import csv
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["department"]   # the department for this person
                int(row["salary"])  # salary as a number (it comes in as text)
    • Group with a normal dict, e.g. totals[dept] and counts[dept],
      or use collections.defaultdict(list) to gather salaries per department.
    • Average = total salary in a department / number of people in it.
    • Track the top earner as you go: compare each salary to the best so far.
============================================================================
"""
import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "employees.csv"


def main() -> None:
    # TODO 1: open CSV_PATH with csv.DictReader and read all the rows


    # TODO 2: build up, per department, the total salary and the head count


    # TODO 3: print each department with its head count and average salary


    # TODO 4: find and print the highest-paid person overall (name + salary)

    # Remove this line once you start writing your solution above:
    print("Not finished yet - complete the # TODO steps in this file.")


if __name__ == "__main__":
    main()
