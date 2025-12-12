from itertools import cycle, pairwise
import turtle as tl

testing = False
if testing:
    fn = "data/test_data"
else:
    fn = "data/day4"


def square_spiralise(i, j, side):
    yield i, j
    visited = (
        [(i, j)]
        + [(j, -1) for j in range(side)]
        + [(-1, j) for j in range(side)]
        + [(side, j) for j in range(side)]
        + [(j, side) for j in range(side)]
    )
    n = 1
    for direction in cycle("NESW"):
        if n == side**2:
            break
        while n < side**2:
            if direction == "E":
                if (i + 1, j) in visited:
                    break
                i += 1
            elif direction == "S":
                if (i, j + 1) in visited:
                    break
                j += 1
            elif direction == "W":
                if (i - 1, j) in visited:
                    break
                i -= 1
            elif direction == "N":
                if (i, j - 1) in visited:
                    break
                j -= 1

            yield i, j
            visited.append((i, j))
            n += 1


def adjacent(i, j, side):
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if not di and not dj:
                continue
            x = i + di
            y = j + dj
            if 0 <= x < side and 0 <= y < side:
                yield x, y


def total_adj(rolls, i, j, side):
    t = 0
    if not rolls[i][j]:
        return -1
    return sum(rolls[x][y] for x, y in adjacent(i, j, side))


def print_rolls(rolls):
    print("")
    for row in rolls:
        for itm in row:
            itm = itm if itm != -1 else 0
            print(f"{itm:2}", end="")
        print("")
    print("")


rolls = []
with open(fn) as f:
    for row in f:
        row = row.strip("\n")
        rolls.append([1 if sym == "@" else 0 for sym in row])

print_rolls(rolls)

side = len(rolls)

adj = [[0 for _ in range(side)] for _ in range(side)]
total = 0
max_adj = 4

while True:
    removed = []
    print(total)
    # print_rolls(rolls)
    for i, j in square_spiralise(0, 0, side):
        t = total_adj(rolls, i, j, side)
        if 0 <= t < max_adj:
            total += 1
            removed.append((i, j))
        adj[i][j] = t
    if not removed:
        break
    for i, j in removed:
        rolls[i][j] = 0

print_rolls(adj)

print(f"There are {total} rolls adjacent with less than {max_adj} neighbours")
