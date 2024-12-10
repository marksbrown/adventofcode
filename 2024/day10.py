import heapq
from itertools import product
fn = "test_data"
fn = "test_data_2"
fn = "test_data_3"
fn = "data"

step = 1

tmap = []
trail_heads = []
trail_tails = []
with open(fn) as f:
    for j, row in enumerate(f):
        row = row.strip('\n')
        new_row = []
        for i, height in enumerate(row):
            if height == ".":
                new_row.append(-1)
            else:
                new_row.append(int(height))
            if height == '0':
                trail_heads.append((j, i))
            if height == '9':
                trail_tails.append((j, i))
        tmap.append(new_row)

extentx = i
extenty = j

def pprint(map_):
    for row in map_:
        for sym in row:
            print(f"{sym:>2}", end="")
        print("")

def valid_steps(tmap, i, j):
    if i > 0:
        if tmap[i][j] != ".":
            yield (i-1, j)
    if i < extentx:
        if tmap[i][j] != ".":
            yield (i+1, j)
    if j > 0:
        if tmap[i][j] != ".":
            yield (i, j-1)
    if j < extenty:
        if tmap[i][j] != ".":
            yield (i, j+1)

def lousy_dijiskra(tmap, start, end):
    heap = [(0, start, None),]  # height, (i,j), from
    heapq.heapify(heap)
    t = 0
    while heap:
        current_height, (i, j), prev = heapq.heappop(heap)
        if (i, j) == end:
            t += 1
        for x,y in valid_steps(tmap, i, j):
            new_height = tmap[x][y]
            if new_height - current_height == step:
                heapq.heappush(heap, (new_height, (x,y), (i,j)))
    return t 


print(f"Map is ({extentx}, {extenty}) in size") 
pprint(tmap)
total = 0
ratings = {}
for start_loc, end_loc in product(trail_heads, trail_tails):
    if start_loc not in ratings:
        ratings[start_loc] = 0
    print(f"starting location of {start_loc} finishing at {end_loc}")
    r = lousy_dijiskra(tmap, start_loc, end_loc)
    if r > 0:
        total += 1
        ratings[start_loc] += r

print(f"There are {total} valid routes from heads to tails")
for rating in ratings:
    print(rating, ratings[rating])

print(f"The total of all ratings is {sum(ratings[r] for r in ratings)}")
