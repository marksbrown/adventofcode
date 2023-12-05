from useful import load_data_gen


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


total = 0
for row in load_data_gen(fn, testing):
    game_id, data = parse_game(row)

    print(game_id, row, data, valid_game(data), sep="\n", end="\n\n")
    if valid_game(data):
        print(game_id, data)
        total += game_id
print(f"Total of game_ids is {total}")
