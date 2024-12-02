from useful import load_data_gen
from string import ascii_lowercase, digits
from warnings import warn
from random import random
from time import sleep

fn = "day1"
testing = False

written_digits = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
)


def parse(v):
    """
    >>> parse("1abc2")
    '12'
    >>> parse("two1nine")
    '219'
    >>> parse("eightwothree")
    '823'
    >>> parse("abcone2threexyz")
    '123'
    >>> parse("treb7uchet")
    '7'
    >>> parse("4nineeightseven2")
    '49872'
    >>> parse("ftjjqbgphtmhthreesix1six")
    '3616'
    """
    values = []
    for j, sym in enumerate(v):
        if sym in digits:
            values.append(sym)
        for digit in written_digits:
            if digit in v[j : j + len(digit)]:
                values.append(str(written_digits.index(digit)))

    return "".join(values)


if testing:
    import doctest

    doctest.testmod()

result = 0
for r in load_data_gen(fn, testing):
    values = parse(r)
    value = int(values[0] + values[-1])
    result += int(value)

print(result)
