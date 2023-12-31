from useful import load_data_gen
from itertools import product, repeat, cycle
import re


def is_match(left, right):
    """
    >>> is_match("#?#", "#.#")
    True
    >>> is_match("#.#", "#?#")
    True
    >>> is_match("##???", "##.##")
    True
    """
    if len(left) != len(right):
        return False
    elif left == right:
        return True

    for l, r in zip(left, right):
        if l == "?" or r == "?":
            continue
        if l != r:
            return False
    return True


fn = "day12"
testing = False
verbose = False


def load_data():
    for row in load_data_gen(fn, testing):
        left, right = row.split(" ")
        right = tuple(map(int, right.lstrip(" ").rstrip(" ").split(",")))
        yield left, right


def count_repetitions(seq):
    count = 0
    prev = None
    for sym in seq:
        if prev is None:
            prev = sym
        if prev == sym:
            count += 1
        else:
            yield prev, count
            count = 1
        prev = sym
    yield prev, count


def count_defective(seq):
    """
    >>> count_defective("#.#.###")
    (1, 1, 3)
    >>> count_defective(".#.###.#.######")
    (1, 3, 1, 6)
    """
    return tuple(count for sym, count in count_repetitions(seq) if sym == "#")


def generate_all_cases(seq):
    """

    >>> list(generate_all_cases("#.#"))
    ['#.#']
    >>> list(generate_all_cases("#?#"))
    ['###', '#.#']
    >>> list(generate_all_cases('??'))
    ['##', '#.', '.#', '..']
    """
    products = []
    for sym, count in count_repetitions(seq):
        if sym in ".#":
            products.append(
                [
                    sym * count,
                ]
            )
        else:
            products.append(["".join(t) for t in product("#.", repeat=count)])
    for p in product(*products):
        yield "".join(p)


if testing:
    import doctest

    doctest.testmod()

# left - str sequence of .#?
# right - int sequence of expected repetitions

total = 0
for left, right in load_data():
    arrangements = 0
    for candidate in generate_all_cases(left):
        if count_defective(candidate) == right:
            arrangements += 1
            if verbose:
                print(candidate, count_defective(candidate))
    if verbose:
        print(left, right, arrangements)
    total += arrangements

print(f"This gives a total of {total}")
