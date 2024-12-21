import re
from itertools import combinations_with_replacement 
from PIL import Image

fn = "test_data"
fn = "data"

if fn == "test_data":
    extentx = 11
    extenty = 7
elif fn == "data":
    extentx = 101
    extenty = 103
else:
    raise NotImplementedError("wat")

def in_bound(x,y) -> bool:
    return 0 <= x < extentx and 0 <= y < extenty

robots = []
with open(fn) as f:
    for row in f:
        row = row.strip('\n')
        if not row:
            continue
        p, v = row.split(' ')
        new_robot = {lbl : list(map(int, re.findall("-?[0-9]+", d))) for lbl, d in (('p', p), ('v', v))}
        robots.append(new_robot)

def step(p, v, steps = 100):
    ext = (extentx, extenty)
    for j in range(len(p)):
        p[j] += v[j] * steps
        p[j] %= ext[j]
    return p

steps = 100
locs = {}
for robot in robots:
    x,y = step(robot['p'], robot['v'], steps)
    if (x,y) not in locs:
        locs[(x,y)] = 1
    else:
        locs[(x,y)] += 1

def quad(i,j) -> int:
    midx = extentx // 2
    midy = extenty // 2
    if i < midx and j < midy:
        return 1
    if i > midx and j > midy:
        return 2
    if i < midx and j > midy:
        return 3
    if i > midx and j < midy:
        return 4
    elif i == midx and j == midy:
        return 0

quads = [0,0,0,0,0]
for j in range(extenty):
    for i in range(extentx):
        if j == extenty // 2:
            print("")
            break
        if i == extentx // 2:
            print(" ", end="")
            continue
        if (i,j) in locs:
            quads[quad(i,j)] += locs[(i,j)]
            print(locs[(i,j)], end="")
        else:
            print(".", end="")
    else:
        print("")


print(quads)
t = 1
for v in quads[1:]:
    t *= v
print(t)
