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


def prev_in_sequence(seq):
    return next_in_sequence(seq[::-1])


def next_in_sequence(seq):
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

first_total = 0
second_total = 0
for seq in sequences:
    r = next_in_sequence(seq)
    first_total += r
    w = prev_in_sequence(seq)
    second_total += w
    if verbose:
        print(seq, *get_next_sequence(seq), sep=" -> ")
        print("prev in sequence", w)
        print("next in sequence", r)

print(f"The totals are {first_total}, {second_total}")
