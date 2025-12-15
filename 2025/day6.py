import re
from functools import reduce
from numpy import transpose

testing = False

if testing:
    fn = "data/test_data"
else:
    fn = "data/day6"

op = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
}

lines = []
operations = []
with open(fn) as f:
    for line in f:
        line = line.strip("\n")
        line = [t for t in re.split("\s+", line) if t]
        if line[0] in op.keys():
            operations = line
        else:
            line = list(map(int, line))
            lines.append(line)

lines = transpose(lines)

# part a
total = 0
for j, line in enumerate(lines):
    print(line, operations[j], "=", end=" ")
    t = reduce(op[operations[j]], line)
    print(t)
    total += t

print("Grand total of ", total)
