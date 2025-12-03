import doctest
from itertools import batched

testing = False

if testing:
    fn = "data/test_data"
else:
    fn = "data/day2"


def parse(seq):
    l, r = seq.split("-")
    return int(l), int(r)


def count(subseq: str, seq: str) -> int:
    """
    >>> count('1', '11')
    2
    >>> count('1', '111')
    3
    >>> count('12', '121212')
    3
    >>> count('123', '1234')
    1
    >>> count('21', '123')
    0
    """
    c = 0
    for s in batched(seq, n=len(subseq)):
        s = "".join(s)
        if s == subseq:
            c += 1
    return c


def is_valid(v) -> bool:
    """
    >>> is_valid("11")
    False
    >>> is_valid("121")
    True
    >>> is_valid("1212")
    False
    >>> is_valid("131131")
    False
    >>> is_valid("110")
    True
    >>> is_valid("1100")
    True
    """
    v = str(v)
    l = len(v)

    n = 1
    while n < l:
        if count(v[:n], v) == l / n:
            return False
        n += 1
    return True


doctest.testmod()

total = 0
with open(fn) as f:
    for line in f:
        line = line.strip("\n")
        for seq in line.split(","):
            if seq:
                low, high = parse(seq)
                print(f"{low}-{high} has invalid IDs:", end=" ")
                for seq in range(low, high + 1):
                    if not is_valid(seq):
                        print(seq, end=" ")
                        total += seq
                print("")
print(total)
