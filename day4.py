from useful import load_data_gen
import re

testing = False
fn = "day4"


def parse_row(row):
    left, right = row.split(":")
    middle, right = right.split("|")
    left = int(re.findall("Card\s*(\d+)", left)[0])
    middle = middle.lstrip(" ").rstrip(" ")
    right = right.lstrip(" ").rstrip(" ")
    middle = set(map(int, re.split("\s+", middle)))
    right = set(map(int, re.split("\s+", right)))
    return left, middle, right


extra_cards = {}
total = 0
for row in load_data_gen(fn, testing):
    k, m, r = parse_row(row)
    if k in extra_cards:
        extra_cards[k] += 1
    else:
        extra_cards[k] = 1  # we only have one of this card
    print("start", extra_cards)
    n = m.intersection(r)
    wins = len(n)
    for j in range(k + 1, k + wins + 1):
        if j not in extra_cards:
            extra_cards[j] = extra_cards[k]
        else:
            extra_cards[j] += extra_cards[k]

    print(f"Card {k} has {wins} wins and there are {extra_cards[k]} cards")
    print("end", extra_cards)
    total += extra_cards.pop(k)

print(total)
