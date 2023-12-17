from useful import load_data_gen
from itertools import zip_longest
from math import sqrt, gcd, floor

fn = "day6"
testing = False


def ceiling(v):
    """
    >>> ceiling(14.2)
    15
    >>> ceiling(14.0001)
    15
    >>> ceiling(14.999)
    15
    """
    if v > floor(v):
        return floor(v) + 1
    else:
        return floor(v)


def actual_solve(d, T):
    """
    Of course this is a trivial physics problem so let's just solve it that way
    """
    dt = sqrt(T**2 - 4 * d)
    t2 = (T + dt) / 2
    t1 = (T - dt) / 2
    return t1, t2


def load_data():
    for row in load_data_gen(fn, testing):
        row = row.strip("\n")
        name, values = row.split(":")
        values = values.rstrip(" ").lstrip(" ")
        values = [int(x) for x in values.split(" ") if x]
        yield name, values


partA = False
raw = {k: v for k, v in load_data()}

data = []
if partA:
    for k in raw:
        data.append(raw[k])
else:
    actual_time = int("".join(map(str, raw["Time"])))
    actual_dist = int("".join(map(str, raw["Distance"])))
    data.append(
        [
            actual_time,
        ]
    )
    data.append(
        [
            actual_dist,
        ]
    )


easier_result = 1
skip_old_method = True
for time, dist in zip(*data):
    print(time, dist)
    t1, t2 = actual_solve(dist, time)
    print(f"Analytical solution provides {t1} and {t2}")
    w_high = ceiling(t2) - floor(t1)
    w_low = floor(t2) - ceiling(t1)
    print(f"Giving a possible range of {w_low} to {w_high}")
    if w_low == w_high:
        w = w_low - 1
    else:
        w = (w_low + w_high) // 2
    easier_result *= w

print(easier_result)
