from useful import load_data_gen

fn = "day11"
testing = False

xs = []
ys = []
for j, row in enumerate(load_data_gen(fn, testing)):
    for i, v in enumerate(row):
        if v == "#":
            xs.append(i)
            ys.append(j)

xm = i
ym = j

rows = [i for i in range(xm + 1) if i not in xs]
cols = [j for j in range(ym + 1) if j not in ys]


def adjust(star, empty_rows, empty_cols, dv=1):
    """
    empty rows and cols are doubled
    """
    x, y = star
    dx = 0
    dy = 0
    for i in empty_rows:
        if i < x:
            dx += dv
    for j in empty_cols:
        if j < y:
            dy += dv

    return x + dx, y + dy


def manhatten_dist(p1, p2):
    t = 0
    for x1, x2 in zip(p1, p2):
        t += abs(x2 - x1)
    return t


print("No stars in rows", rows, "or in cols", cols)
from itertools import combinations

# part B
dv = int(1e6) - 1  # I dunno why
stars = zip(xs, ys)
stars = list(map(lambda coord: adjust(coord, rows, cols, dv), zip(xs, ys)))
r = 0
for j, (p1, p2) in enumerate(combinations(stars, r=2)):
    r1 = manhatten_dist(p1, p2)
    print(j, p1, p2, r1)
    r += r1

print(f"The total sum of all steps is {r}")
