

fn = "test_data"
fn = "test_data_2"
fn = "data"
fn = "test_data_3"

plants = {}  # ID : [(loc), ...]
with open(fn) as f:
    for j, row in enumerate(f):
        row = row.strip('\n')
        if 'test_data' in fn:
            print(row)
        for i, plant in enumerate(row):
            if plant not in plants:
                plants[plant] = [(i,j),]
            else:
                plants[plant].append((i,j))

extentx = i + 1
extenty = j + 1

def adj(i,j):
    if i < extentx:
        yield i+1, j
    if i > 0:
        yield i-1, j
    if j < extenty:
        yield i, j+1
    if j > 0:
        yield i, j-1

garden_graph = {}
for plant in plants:
    for i,j in plants[plant]:
        garden_graph[(i,j)] = tuple(filter(lambda pos : pos in plants[plant], adj(i,j)))
    
garden_map = {}
for plant in plants:
    for i,j in plants[plant]:
        garden_map[(i,j)] = plant

# for node in garden_graph:
#     print(f"{node} ({garden_map[node]}) is connected to {garden_graph[node]}")

# find distinct regions
# Need to visit each node and traverse to all via the graph
# from here we produce a set of regions which we will then calculate area and perimeters from
def bfs(start, graph):
    visited = []
    to_visit = [start,]
    while to_visit:
        current = to_visit.pop(0)
        visited.append(current)
        for candidate in graph[current]:
            if candidate not in visited and candidate not in to_visit:
                to_visit.append(candidate)
        yield current
        

def find_perimeter(nodes):
    """
    Each node starts with 4 fences
    For each adjacent node we reduce this number by 1
    """
    perimeter = 0
    for node in nodes:
        sides = 4
        for i,j in adj(*node):
            if (i,j) in nodes:
                sides -= 1
        perimeter += sides
    return perimeter
        
def adj_NESW(i,j):
    if i < extentx:
        yield 'E', i+1, j
    if i > 0:
        yield 'W', i-1, j
    if j < extenty:
        yield 'S', i, j+1
    if j > 0:
        yield 'N', i, j-1


def find_corners(nodes):
    fences = {}
    # Need to visit all cells around the region too
    sides = "NESW"
    for node in nodes:
        fences[node] = list(sides)
        for d, i, j in adj_NESW(*node):
            if (i,j) in nodes:
                fences[node].pop(fences[node].index(d))
            else:
                if (i,j) not in fences:
                    fences[(i,j)] = [d,]
                else:
                    fences[(i,j)].append(d)
    count = 0
    for node in fences:
        # print(f"Node: {node} : {fences[node]}")
        for corners in ('NW', 'NE', 'SE', 'SW'):
            if all(d in fences[node] for d in corners):
                count += 1
    return count 

regions = []
visited = []
for node in garden_graph:
    plant = garden_map[node]
    if node not in visited:
        new_region = tuple(bfs(node, garden_graph))
        regions.append({'plant' : plant,
                        'region' : new_region,
                        'area' : len(new_region), 
                        'perimeter' : find_perimeter(new_region),
                        'corners' : find_corners(new_region)})
        visited += new_region

total = 0
discounted_total = 0
for region in regions:
    price = region['area'] * region['perimeter']
    # print(f"A region of '{region['plant']}' plants with price {region['area']} * {region['perimeter']} = {price}")
    total += price
    discounted_price = region['area'] * region['corners']
    discounted_total += discounted_price
    print(f"A region of '{region['plant']}' plants with price {region['area']} * {region['corners']} = {discounted_price}")

print(f"This gives a total price of {total}")
print(f"This gives a total discounted price of {discounted_total}")
