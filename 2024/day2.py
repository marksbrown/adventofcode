import re
from collections import Counter
from itertools import pairwise

fn = "test_data"
fn = "data"


def is_safe(report) -> bool:
    all_ascending = all(a > b for a, b in pairwise(report))
    all_descending = all(a < b for a, b in pairwise(report))
    safe_deltas = all(1 <= abs(a - b) <= 3 for a, b in pairwise(report))
    safe = (all_descending or all_ascending) and safe_deltas
    return safe


total_safe = 0
enable_dampener = True
with open(fn) as f:
    for report in f:
        report = report.strip("\n").split(" ")
        report = list(map(int, report))
        r = is_safe(report)
        if not r and enable_dampener:
            # check every permutation excluding a single value
            for j in range(len(report)):
                r = is_safe(report[:j] + report[j + 1 :])
                if r:
                    total_safe += 1
                    break
        else:
            total_safe += 1


print(f"There are {total_safe} safe reactors")
