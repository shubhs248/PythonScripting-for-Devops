#!/usr/bin/env python3
"""Solution — Exercise 2.2 CSV Report"""
import csv
from collections import defaultdict
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "employees.csv"


def main() -> None:
    salaries_by_dept = defaultdict(list)
    top_earner = {"name": None, "salary": 0}

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row["department"]
            salary = int(row["salary"])
            salaries_by_dept[dept].append(salary)

            if salary > top_earner["salary"]:
                top_earner = {"name": row["name"], "salary": salary}

    print("Report by department")
    print("-" * 40)
    for dept in sorted(salaries_by_dept):
        salaries = salaries_by_dept[dept]
        headcount = len(salaries)
        average = sum(salaries) / headcount
        print(f"{dept:<12} people: {headcount:<3} avg salary: {average:,.0f}")

    print("-" * 40)
    print(f"Top earner: {top_earner['name']} ({top_earner['salary']:,})")


if __name__ == "__main__":
    main()
