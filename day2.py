from useful import load_data_gen
from itertools import product


def parse_game(game: str):
    num, data = row.split(":")
    num = int(num.split(" ")[-1])

    def f(single_round):
        for r in single_round:
            data = {}
            for x in r.split(","):
                x = x.lstrip(" ").rstrip(" ")
                num, col = x.split(" ")
                data[col] = int(num)
            yield data

    return num, list(f(data.split(";")))


def total(game):
    """
    totals of all colours used in a game
    >>> total([{"blue" : 3, "red" : 4}, {"red" : 1, "blue" : 2}, {"green" : 1}])
    {'blue': 5, 'red': 5, 'green': 1}
    """
    result = {}
    for r in game:
        for col in r:
            if col not in result:
                result[col] = r[col]
            else:
                result[col] += r[col]

    return result


def min_cols(game):
    """
    Find minimum number of each colour needed to complete this game
    >>> min_cols([{"blue" : 3, "red" : 4}, {"red" : 1, "blue" : 2}, {"green" : 1}])
    {'blue': 3, 'red': 4, 'green': 1}
    """
    result = {}
    for r in game:
        for col in r:
            if col not in result:
                result[col] = r[col]
            elif r[col] > result[col]:
                result[col] = r[col]

    return result


def power(r):
    """
    Multiply all colours together
    >>> power({'blue': 6, 'red': 4, 'green': 2})
    48
    """
    t = 1
    for k in r:
        t *= r[k]

    return t


testing = False
fn = "day2"


def valid_game(games) -> bool:
    """
    determine if game is possible with specified max_cubes
    """
    max_cubes = {"red": 12, "blue": 14, "green": 13}

    for game in games:
        if not all(game.get(col, 0) <= max_cubes[col] for col in max_cubes):
            return False

    return True


if testing:
    import doctest

    doctest.testmod()

total = 0
power_total = 0
for row in load_data_gen(fn, testing):
    game_id, data = parse_game(row)

    min_balls = min_cols(data)
    t = power(min_balls)
    print(f"{min_balls} gives {t}")
    power_total += t
    if valid_game(data):
        total += game_id
print(f"Total of game_ids is {total}")
print(f"The total of power applied to min balls is {power_total}")
