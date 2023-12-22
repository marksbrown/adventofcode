from useful import load_data_gen
from itertools import pairwise

fn = "day9"
testing = False
verbose = False


def diff(seq):
    for x, y in pairwise(seq):
        yield y - x


sequences = [tuple(map(int, row.split(" "))) for row in load_data_gen(fn, testing)]


def arith_next(seq):
    *_, pprev, prev = seq
    return (prev - pprev) + prev


def next_in_sequence(seq, last_term=None):
    """
    Determine next in sequence for a polynomial sequence
    (arithmetic, quadratic, ...)
    >>> next_in_sequence((0, 3, 6, 9, 12, 15))
    18
    >>> next_in_sequence((1, 3, 6, 10, 15, 21))
    28
    >>> next_in_sequence((10, 13, 16, 21, 30, 45))
    68
    """
    v = seq[-1]
    for x in get_next_sequence(seq):
        v += x[-1]

    return v


def get_next_sequence(seq):
    current = seq
    while True:
        current = tuple(diff(current))
        if not any(current):
            break
        yield current


if testing:
    import doctest

    doctest.testmod()

total = 0
for seq in sequences:
    r = next_in_sequence(seq)
    total += r
    if verbose:
        print(seq, *get_next_sequence(seq), sep=" -> ")
        print(next_in_sequence(seq))

print(f"The total is {total}")
