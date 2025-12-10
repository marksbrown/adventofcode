testing = False
if testing:
    fn = "data/test_data"
else:
    fn = "data/day4"


rolls = []
lim = []

with open(fn) as f:
    for j, row in enumerate(f):
        row = row.strip("\n")
        for i, sym in enumerate(row):
            if sym == "@":
                rolls.append((i, j))
    lim = [i, j]


def count_adj(x, y):
    global lim
    c = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if not di and not dj:
                continue
            i = x + di
            j = y + dj
            if 0 <= i <= lim[0] and 0 <= j <= lim[1]:
                if (i, j) in rolls:
                    c += 1
    return c


max_rolls = 4
valid = sum(count_adj(*c) < max_rolls for c in rolls)
print(f"There are {valid} valid rolls")
