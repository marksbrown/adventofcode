testing = False
if testing:
    fn = "data/test_data"
else:
    fn = "data/day4"


def total_adj(rolls, i, j, limx, limy):
    t = 0
    if not rolls[i][j]:
        return -1
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if not di and not dj:
                continue
            x = i + di
            y = j + dj
            if 0 <= x < limx and 0 <= y < limy:
                t += rolls[x][y]
    return t


rolls = []

with open(fn) as f:
    for row in f:
        row = row.strip("\n")
        rolls.append([1 if sym == "@" else 0 for sym in row])

print(*rolls, sep="\n")

limy = len(rolls)
limx = len(rolls[0])

adj = [[0 for _ in range(limx)] for _ in range(limy)]
total = 0
max_adj = 4

j = 0
while j < limy:
    i = 0
    while i < limx:
        t = total_adj(rolls, i, j, limx, limy)
        if 0 <= t < max_adj:
            total += 1
        adj[i][j] += t
        i += 1
    j += 1

print("", *adj, sep="\n")
print(f"There are {total} rolls adjacent with less than {max_adj} neighbours")
