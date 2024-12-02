from useful import load_data_gen
import re
from itertools import cycle
from math import lcm
from collections import Counter

fn = "day8"
testing = False


def load_graph():
    graph = {}
    for j, row in enumerate(load_data_gen(fn, testing)):
        if not j:
            route = row.strip("\n")
        for d in re.findall("(\w+) = \((\w+), (\w+)\)", row):
            k, l, r = d
            graph[k] = {"L": l, "R": r}
    return route, graph


route, graph = load_graph()

starting_nodes = []
end_nodes = []
for k in graph:
    if k.endswith("A"):
        starting_nodes.append(k)
    elif k.endswith("Z"):
        end_nodes.append(k)
    print(k, graph[k])


def move(start_at, route):
    N = len(route)
    current = start_at
    while True:
        for j in range(N):
            next_move = route[j]
            next_loc = graph[current][next_move]
            yield next_loc
            current = next_loc


print(f"Route is '{route}'")

print(starting_nodes, end_nodes, sep="\n")
count = 0
all_finished = False
ghosts = tuple(move(node, route) for node in starting_nodes)
N = 100000
visited = {}
while not all_finished:
    count += 1
    for j in range(len(ghosts)):
        x = next(ghosts[j])

        if x in end_nodes:
            if j not in visited:
                visited[j] = count
    if count > N:
        break

from math import lcm

N = len(route)
visited = [x // N for x in visited.values()]
print(visited)
r = lcm(*visited)
print(r, r * N)
