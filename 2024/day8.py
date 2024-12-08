from itertools import combinations, chain
fn = "test_data"
fn = "data"

antennae = {}
with open(fn) as f:
    for j, row in enumerate(f):
        row = row.strip('\n')
        for i, itm in enumerate(row):
            if itm != '.':
                if itm not in antennae:
                    antennae[itm] = [(i,j),]
                else:
                    antennae[itm].append((i,j))

L = 100  # technical bodge factor

extentx = i + 1
extenty = j + 1

antinodes = []
for antenna in antennae:
    for (x1, y1), (x2, y2) in combinations(antennae[antenna], r=2):
        dx = x2 - x1
        dy = y2 - y1
         
        f = ((n*dx + x2, n*dy + y2) for n in chain(range(-L, 0), range(1, L+1)))
        s = ((x1 - n*dx, y1 - n*dy) for n in chain(range(-L, 0), range(1, L+1)))
        for c in (*f,*s):
            if 0 <= c[0] < extentx and 0 <= c[1] < extenty:
                antinodes.append(c)

print(f"We have found {len(set(antinodes))} antinodes")
