from itertools import pairwise

testing = False

if testing:
    fn = "data/test_data"
else:
    fn = "data/day3"


def find_maximum_joltage(seq: str):
    if len(seq) < 2:
        return 0

    l = 0
    l = seq.index(max(seq[:-1]))
    max_joltage = seq[l] + seq[l + 1]
    for r in range(l + 1, len(seq)):
        nv = seq[l] + seq[r]
        if nv > max_joltage:
            max_joltage = nv

    return max_joltage


total_joltage = 0
with open(fn) as f:
    for voltages in f:
        voltages = voltages.strip("\n")
        v = int(find_maximum_joltage(voltages))
        print(voltages, v)
        total_joltage += v
print(total_joltage)
