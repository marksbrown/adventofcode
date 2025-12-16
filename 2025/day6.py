import re
from itertools import pairwise
from functools import reduce
from numpy import array, rot90

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

with open(fn) as f:
    for line in f:
        line = line.strip("\n")

spacings = [
    0,
]
operations = []
for j, elem in enumerate(line):
    if elem in op:
        operations.append(elem)
        if j:
            spacings.append(j)
else:
    spacings.append(len(line) + 1)

lines = []
row = {}
with open(fn) as f:
    for line in f:
        line = line.replace("\n", "0")
        if line[0] in op.keys():
            break
        for z, (l, r) in enumerate(pairwise(spacings)):
            # print(line[l:r], end="|")
            seq = line[l : r - 1]  # .replace(' ', '0')
            seq = seq.strip("\s")
            print(seq, end="|")
            if not seq:
                seq = [
                    0,
                ]
            if z not in row:
                row[z] = [
                    list(seq),
                ]
            else:
                row[z].append(list(seq))
            z += 1
        lines.append(row)
        print("")
print(operations)
print("===")

lines = []
for line in row:
    arr = array(row[line])
    arr = rot90(arr)
    lines.append(list(map(lambda x: int("".join(x)), arr)))

total = 0
for j, line in enumerate(lines):
    print(line, operations[j], "=", end=" ")
    t = reduce(op[operations[j]], line)
    print(t)
    total += t

print("Grand total of ", total)
