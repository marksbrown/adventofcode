from useful import load_data_gen
from string import digits

testing = False
fn = "day3"


def load_data():
    return list(load_data_gen(fn, testing))


def find_symbols_gen(data):
    """
    Find coordinates of anything that isn't a digit or a .
    """
    ignore = digits + "."
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y not in ignore:
                yield i, j


def get_all_adjacent_gen(x, y, maxx, maxy):
    """
    get all adjacent (valid) coordinates
    """
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if 0 <= x + dx < maxx and 0 <= y + dy < maxy:
                yield x + dx, y + dy


def get_values_horizontal(data):
    """
    Find all groups of digits in data
    """
    for i, row in enumerate(data):
        current = []
        coords = []
        for j, sym in enumerate(row):
            if sym in digits:
                current.append(sym)
                coords.append((i, j))
            elif current:
                yield int("".join(current)), coords
                current = []
                coords = []
        if current:
            yield int("".join(current)), coords


ignore = digits + "."
data = load_data()

maxy = len(data)
maxx = len(data[0])

symbols = list(find_symbols_gen(data))

total = 0

for v, coords in get_values_horizontal(data):
    symbol_found = False
    for x, y in coords:
        for i, j in get_all_adjacent_gen(x, y, maxx, maxy):
            if (i, j) in symbols:
                symbol_found = True
                break

        if symbol_found:
            break

    if symbol_found:
        total += v
    else:
        print(f"{v} is not adjacent to a coordinate")

print(f"Total of part numbers is {total}")
