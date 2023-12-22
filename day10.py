"""
The pipes are arranged in a two-dimensional grid of tiles:

    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
from useful import load_data_gen

fn = "day10"
testing = False
verbose = False


def parse(x, y, sym):
    if sym == "|":
        return (x, y - 1), (x, y + 1)
    elif sym == "-":
        return (x - 1, y), (x + 1, y)
    elif sym == "L":
        return (x, y - 1), (x + 1, y)
    elif sym == "J":
        return (x, y - 1), (x - 1, y)
    elif sym == "7":
        return (x, y + 1), (x - 1, y)
    elif sym == "F":
        return (x, y + 1), (x + 1, y)
    else:
        return ()


def get_raw_maze():
    maze = []
    for row in load_data_gen(fn, testing):
        if row == "=":
            yield maze
            maze = []
            continue
        maze.append(row)


def adjacent_coords(x, y, maxx, maxy):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if not i and not j:
                continue
            newx = x + i
            newy = y + j
            if 0 <= newx < maxx and 0 <= newy < maxy:
                yield newx, newy


def maze_to_graph(maze):
    graph = {}
    for j, row in enumerate(maze):
        for i, v in enumerate(row):
            if v == "S":
                graph["start"] = (i, j)
                continue
            valid_locations = adjacent_coords(i, j, len(maze[0]), len(maze))

            locs = parse(i, j, v)
            locs = tuple(locs)
            if locs:
                graph[(i, j)] = locs

    graph[graph["start"]] = tuple(filter(lambda k: graph["start"] in graph[k], graph))
    return graph


def is_loop(path):
    return path[0] == path[-1]


def flood_fill(graph, start_at):
    paths = [[start_at, k] for k in graph[start_at]]
    loop_found = False
    while not loop_found:
        if not paths:
            print("No loop found!")
            break
        current = paths.pop(0)
        for dest in graph[current[-1]]:
            if dest != current[-2]:
                paths.append(
                    current
                    + [
                        dest,
                    ]
                )
                if dest == start_at:
                    loop_found = True

    return paths[-1]


for maze in get_raw_maze():
    print(*maze, sep="\n")
    graph = maze_to_graph(maze)
    r = flood_fill(graph, graph["start"])
    print(r)
    N = (len(r) - 1) // 2
    print("Furthest away is ", N)
