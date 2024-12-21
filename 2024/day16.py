from functools import cache
from itertools import pairwise
import heapq

fn = "test_data"
fn = "test_data_2"
fn = "test_data_4"
fn = "test_data_3"
fn = "data"

valid_symbols = ".ES"

raw_data = []
with open(fn) as f:
    for row in f:
        row = row.strip('\n')
        raw_data.append(row)

extentx = len(raw_data[0])
extenty = len(raw_data)
def adj(i,j):
    if i > 0:
        yield i-1, j
    if i < extentx:
        yield i+1, j
    if j > 0:
        yield i, j-1
    if j < extenty:
        yield i, j+1

graph = {}  # from, to
for j, row in enumerate(raw_data):
    for i, sym in enumerate(row):
        if sym in valid_symbols:
            graph[(i,j)] = []
            for x,y in adj(i,j):
                if raw_data[y][x] in valid_symbols:
                    graph[(i,j)].append((x,y))
        if sym == "E":
            start_loc = (i, j)
        if sym == "S":
            end_loc = (i, j)

def direction(A, B):
    """
    >>> direction((0,0), (1,0))
    'E'
    >>> direction((1,0), (0,0))
    'W'
    >>> direction((0,0), (0,1))
    'S'
    >>> direction((0,1), (0,0))
    'N'
    """
    i,j = A
    x,y = B
    if j == y: # must be N or S
        if x > i:
            return 'E'
        return 'W'
    elif i == x:
        if y > j:
            return 'S'
        return 'N'
    
    raise ValueError("wat")  # diagonals are bad

@cache
def turn_cost(A, B, add=1000):
    """
    >>> turn_cost('N', 'N')
    0
    >>> turn_cost('N', 'W')
    1000
    >>> turn_cost('N', 'S')
    2000
    >>> turn_cost('E', 'S')
    1000
    >>> turn_cost('S', 'N')
    2000
    >>> turn_cost('W', 'E')
    2000
    """
    if A == B:
        return 0
    angles = {'N' : 0, 'E' : 90, 'S' : 180, 'W' : 270}
    clockwise = angles[B] - angles[A]
    anticlockwise = angles[A] - angles[B]
    x = clockwise % 360 // 90 * add
    y = anticlockwise % 360 // 90 * add
    r = min((x,y))
    return min((x,y))

if 'test_data' in fn:
    import doctest
    doctest.testmod()

print("Starting at", start_loc)
print("Ending at", end_loc)

def weird_dijiskra(start, end):
    to_visit = [(0, start), ]
    heapq.heapify(to_visit)
    nodes = {start : {'prev' : None, 'score' : 0}}
    visited = []
    while to_visit:
        score, current = heapq.heappop(to_visit)
        if current in visited:
            continue

        visited.append(current)
        if current == end:
            return nodes
        for candidate in graph[current]:
            if candidate in visited:
                continue
            
            # 1. Where did we come from?
            prev = nodes[current]['prev']
            if prev is None:
                prev_facing = 'E'
            else:
                prev_facing = direction(prev, current)

            # 2. Did we turn?
            new_facing = direction(current, candidate)

            # 3. What would be the cost to get there?
            new_score = score + 1 + turn_cost(prev_facing, new_facing)
           
            if candidate in nodes:
                if new_score >= nodes[candidate]['score']:
                    continue

            nodes[candidate] = {'prev' : current, 'score' : new_score}
            heapq.heappush(to_visit, (new_score, candidate))
                
                
symbols = {"N": "^", "E" : ">", "S" : "v", "W" : "<"}
path = weird_dijiskra(start_loc, end_loc)
route = [end_loc, ]
current = end_loc
while current != start_loc:
    current = path[current]['prev']
    route.append(current)

route = list(reversed(route))
print(*route, sep=" -> ")
facing = {a : symbols[direction(a,b)] for a,b in pairwise(route)}
print(facing)
total = 1
for a,b in pairwise(route):
    prev = facing[a]
    next_ = facing.get(b, None)
    if next_ is None:
        break
    if prev == next_:
        total += 1
    else:
        total += 1001

print(total)

for j, row in enumerate(raw_data):
    for i, sym in enumerate(row):
        if (i,j) == start_loc:
            print("S", end="")
        elif (i,j) == end_loc:
            print("E", end="")
        elif (i,j) in facing:
            print(facing[(i,j)], end="")
        else:
            print(sym, end="")
    print("")

print(path[end_loc])

