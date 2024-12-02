import re
from collections import Counter

fn = "data"

left = []
right = []
with open(fn) as f:
    for row in f:
        row = row.strip("\n")
        row = re.split(r"\s+", row)
        if len(row) < 2:
            continue
        a, b = row
        left.append(int(a))
        right.append(int(b))

# part 1
dist = sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))
print(dist)

# part 2
right = Counter(right)
score = sum(x * right[x] for x in left)
print(score)
