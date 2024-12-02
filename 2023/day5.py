from useful import load_data_gen
import re
from itertools import chain


pat = re.compile("(\w+)\-to\-(\w+)\smap")
fn = "day5"
testing = True
verbose = True

## loading data
def parse_row(row):
    values = row.split(" ")
    assert len(values) == 3, "errr"
    l, c, r = map(int, values)
    return (l, l + r), (c, c + r)

def as_range(seeds):
    while seeds:
        x = seeds.pop(0)
        dx = seeds.pop(0)
        yield (x,x+dx)

def load_data(fn):
    data = {}
    for j, row in enumerate(load_data_gen(fn, testing)):
        if not j:
            seeds = [int(v) for v in row.split(":")[1].split(" ") if v]
            data["seeds"] = as_range(seeds)
            continue
        if ":" in row:
            x = re.findall(pat, row)[0]
            f, t = x
            data[f] = {t: {}}
        else:
            destination, source = parse_row(row)
            if data[f][t]:
                data[f][t]["source"].append(source)
                data[f][t]["destination"].append(destination)
            else:
                data[f][t] = {
                    "source": [
                        source,
                    ],
                    "destination": [
                        destination,
                    ],
                }
    return data


## Analysing data
def shift(v, left, right):
    """
    move to same relative position in right
    from v in left if in the left range (inclusive)
    >>> shift(5, (1,10), (10, 100))
    14
    >>> shift(5, (10, 20), (1,10))
    5
    """
    low, high = left
    if v < low or v > high:
        return v
    else:
        return right[0] + (v - low)


def step(data, current, value):
    for dest in data[current]:
        if verbose:
            print(f"{current} -> {dest}")
            print(f"{current} number {value} corresponds to ", end="")
        for j, src in enumerate(data[current][dest]["source"]):
            low, high = src
            if low <= value <= high:
                destination = data[current][dest]["destination"][j]
                value = shift(value, src, destination)
                break
        current = dest
        if verbose:
            print(f"{current} number {value}")
        break
    return current, value


def step_seed_range(data, current, a, b):
    """
    Step through a seed range on a single step
    where an unknown number of results is provided
    """
    for dest in data[current]:
        print(f"Checking {current} -> {dest} for {seed_low} -> {seed_high}")
        for low, high in data[current][dest]["source"]:
            if high < a:
                continue
            elif low > b:
                continue
            elif a <= low <= b and b
            while values:
                yield values.pop(0), values.pop(0)

def step_pair(data, current, low, high):
    ns1, nv1 = step(data, current, low)
    ns2, nv2 = step(data, current, high)
    assert ns1 == ns2, "we have to be going to the same places"

    current = ns1
    if nv1 > nv2:
        nv1, nv2 = nv2, nv1

    next_values = list(step_seed_range(data, current, nv1, nv2))
    print(f"These become {next_values}")
    return current, next_values

if __name__ == "__main__":
    if testing:
        import doctest
        doctest.testmod()
    data = load_data(fn)

    results = {}

    current = "seed"
    values = list(data["seeds"])

    print(f"Beginning run")
    print(values)
    while current != "location":
        next_values = []
        print(f"Checks at {current}")
        for seed_low, seed_high in values:
            next_current, v = step_pair(data, current, seed_low, seed_high)
            next_values += v
        values = next_values
        current = next_current
        print(f"Updated to {current} with values {values}")
        break

    1/0
    # must reduce number of seed calculations!
    results = {seed_pair: get_location_number(data, *seed_pair) for seed_pair in seeds}

    for seed in sorted(results, key=lambda k: results[k]):
        print(f"{seed} seed has a location value of {results[seed]} location number")
