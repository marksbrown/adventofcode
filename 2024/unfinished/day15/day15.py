fn = "test_data"
fn = "data"
fn = "test_data_2"

world_map = []
instructions = []
first = True
with open(fn) as f:
    for j, row in enumerate(f):
        row = row.strip('\n')
        if not row:
            first = False
            continue
        if first:
            new_row = []
            for i, sym in enumerate(row):
                new_row.append(sym)
                if sym == "@":
                    robot = (i,j)
            world_map.append(new_row)
        else:
            instructions.append(row)

instructions = "".join(instructions)

def print_map():
    for row in world_map:
        print("".join(row))

extentx = len(world_map[0]) - 1
extenty = len(world_map) - 1

def adj(loc, facing):
    i,j = loc
    if facing == "^":  # N
        if j > 0:
            return i, j-1
    elif facing == "v":  # S
        if j < extenty:
            return i, j+1
    elif facing == "<":  # W
        if i > 0:
            return i-1, j
    elif facing == ">":  # E
        if i < extenty:
            return i+1, j
    else:
        raise NotImplementedError("wat")

def swap(first, second):
    x,y = first
    i,j = second
    if "test_data" in fn:
        print(f"Swap operation occuring: {world_map[y][x]} -> {world_map[j][i]}")
    world_map[j][i], world_map[y][x] = world_map[y][x], world_map[j][i]
    if "test_data" in fn:
        print_map()
    # breakpoint()

def move(loc, facing) -> bool:
    new_loc = adj(loc, facing)
    if new_loc is None:
        return False  # Nowhere to go
    else:
        i,j = new_loc

    if world_map[j][i] == "#":
        return False  # Cannae walk thru walls
    elif world_map[j][i] == "O":
        if move((i,j), facing):  # Can we move a rock?
            swap(loc, (i,j))
            return True
        else:
            return False
    elif world_map[j][i] == ".":
        swap(loc, (i,j))
        return True
    raise ValueError("Undefined Behaviour has occurred!")

print("Initial State")
print_map()
for instruction in instructions:
    print(f"= Attempting to move robot at {robot} with instruction {instruction}")
    if move(robot, instruction):
        robot = adj(robot, instruction)

def calculate_gps():
    total = 0
    for j, row in enumerate(world_map):
        for i, sym in enumerate(row):
            if sym == "O":
                total += 100 * j + i
    return total

print(f"The final score is", calculate_gps())

