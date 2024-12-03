import re
from itertools import pairwise

fn = "test_data"
fn = "data"

output = []
with open(fn) as f:
    for row in f:
        output.append(row.strip("\n"))

raw_input = "".join(output)
pat = r"mul\((\d{1,3}),(\d{1,3})\)"

print("Part A")
r = sum(int(a) * int(b) for a, b in re.findall(pat, raw_input))
print("Result is", r)

print("Part B")
enabled = True
r = 0
for p, q in pairwise(re.finditer(pat, raw_input)):
    i = p.span()[1]
    j = q.span()[0]
    if enabled:
        r += int(p.group(1)) * int(p.group(2))
    if "do()" in raw_input[i:j]:
        enabled = True
    elif "don't()" in raw_input[i:j]:
        enabled = False

if enabled:
    r += int(q.group(1)) * int(q.group(2))

print("Result is", r)
