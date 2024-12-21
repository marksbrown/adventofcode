from itertools import cycle, chain
fn = "test_data_2"
fn = "data"
fn = "test_data"

obstacles = []
visited = []
facing = cycle("NESW")

with open(fn) as f:
    for j, row in enumerate(f):
        row = row.strip('\n')
        for i, sym in enumerate(row):
            if sym == "#":  # obstacle 
                obstacles.append((i,j))
            elif sym == "^":
                visited.append((i,j))

extentx = i+1
extenty = j+1
def get_candidates(t, i, j):
    if t == "N":
        # from (i,j) -> (i, 0)
        yield from [(i,k) for k in range(j-1, -1, -1)]
    elif t == "E":
        # from (i,j) -> (extentx, j)
        yield from [(k,j) for k in range(i+1, extentx)]
    elif t == "S":
        # from (i,j) -> (i, extenty)
        yield from [(i,k) for k in range(j+1, extenty)]
    elif t == "W":
        # from (i,j) -> (0,j)
        yield from [(k,j) for k in range(i-1, -1, -1)]
    else:
        raise ValueError("Wat")

corners = []  # four corners make a loop!
while True:
    i,j = visited[-1]
    t = next(facing)
    hit_wall = False
    for candidate in get_candidates(t, i, j):
        if candidate in obstacles:
            corners.append(candidate)
            hit_wall = True
            break
        else:
            if candidate not in visited:
                visited.append(candidate)

    if not hit_wall:
        break

total = len(visited)
print(visited)
print(f"The guard has visited {total} positions")

from itertools import pairwise

print(corners)
def could_make_loop(first, second, third):
    """
    Rectangles are mercifully aligned to coordinate system
    Thus we can predict what the forth coordinate would be

    Hence we can generate all possible fourth candidates
    Then all we do is check if we ever cross through this location
    If we do, we have a loop!

    So we shall check each direction individually
    """
    fx, fy = first
    sx, sy = second
    tx, ty = third
    east = sorted([fx, sx, tx])
    south = sorted([fy, sy, ty])
    for heading in (east, south):
            r = any(j - i == 1 for i,j in pairwise(heading))
            print(r)
        
    return True


for i in range(len(corners)-2):
    f,s,t = (corners[i+j] for j in (0,1,2))
    print(f,s,t)
    r = could_make_loop(f,s,t)

    
