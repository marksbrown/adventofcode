from itertools import pairwise

testing = False

if testing:
    fn = "data/test_data"
else:
    fn = "data/day3"


def find_maximum_joltage(seq: list, cells: int):
    seq = list(seq)
    r = []
    while len(r) < cells:
        vmax = 9
        while vmax:
            if str(vmax) in seq:
                l = seq.index(str(vmax))
                if l + cells - len(r) <= len(seq):
                    r.append(str(vmax))
                    seq = seq[l + 1 :]
                    break
            vmax -= 1

    return r


total_joltage = 0
with open(fn) as f:
    for voltages in f:
        voltages = voltages.strip("\n")
        print("Initial:", voltages, "->", end=" ")
        v = find_maximum_joltage(voltages, cells=12)
        v = int("".join(v))
        print(v)
        total_joltage += v
print(total_joltage)
