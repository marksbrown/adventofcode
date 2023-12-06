from useful import load_data_gen
import re

testing = False
fn = "day4"


def parse_row(row):
    left, right = row.split(":")
    middle, right = right.split("|")
    left = int(re.findall("Card\s*(\d+)", left)[0])
    middle = middle.lstrip(" ").rstrip(" ")
    right = right.lstrip(" ").rstrip(" ")
    middle = set(map(int, re.split("\s+", middle)))
    right = set(map(int, re.split("\s+", right)))
    return left, middle, right


data = {}
total_points = 0
for row in load_data_gen(fn, testing):
    k, m, r = parse_row(row)
    n = m.intersection(r)
    if not len(n):
        points = 0
    else:
        points = 2 ** (len(m.intersection(r)) - 1)

    data[k] = {"winning": m, "found": r, "points": points}
    total_points += points

print(f"Total points found is {total_points}")
