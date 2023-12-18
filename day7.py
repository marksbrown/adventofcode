from collections import Counter
from useful import load_data_gen

fn = "day7"
testing = False

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
# lowest index is highest strength


def left_card_stronger(left, right):
    li = cards.index(left)
    ri = cards.index(right)
    return li < ri


# determine if hand is valid
# assert len(hand) == 5, "hand must have 5 cards"


def five_of_a_kind(hand):
    """
    >>> five_of_a_kind("AAAAA")
    True
    >>> five_of_a_kind("AAAAB")
    False
    """
    return len(set(hand)) == 1


def four_of_a_kind(hand):
    """
    >>> four_of_a_kind("AAAAB")
    True
    >>> four_of_a_kind("AAABB")
    False
    >>> four_of_a_kind("AABBC")
    False
    """
    count = Counter(hand)
    if len(count) != 2:
        return False
    for k in count:
        if count[k] == 4:
            return True
    return False


def three_of_a_kind(hand):
    """
    >>> three_of_a_kind("AAABC")
    True
    >>> three_of_a_kind("AAAAB")
    False
    >>> three_of_a_kind("ABCAA")
    True
    """
    count = Counter(hand)
    if len(count) < 3:
        return False
    for k in count:
        if count[k] == 3:
            return True

    return False


def full_house(hand):
    """
    >>> full_house("AAABC")
    False
    >>> full_house("ABBCA")
    False
    >>> full_house("AAABB")
    True
    >>> full_house("23332")
    True
    """
    count = Counter(hand)
    if len(count) != 2:
        return False
    for k in count:
        if count[k] == 3:
            return True
    return False


def count_pairs(hand):
    """
    >>> count_pairs("AABBC")
    2
    >>> count_pairs("AACDE")
    1
    """
    count = Counter(hand)
    N = 0
    for k in count:
        if count[k] == 2:
            N += 1

    return N


def two_pairs(hand):
    """
    >>> two_pairs("AABBC")
    True
    >>> two_pairs("AABCD")
    False
    """
    return count_pairs(hand) == 2


def one_pair(hand):
    """
    >>> one_pair("AABBC")
    False
    >>> one_pair("AABCD")
    True
    """
    return count_pairs(hand) == 1


def high_card(hand):
    """
    >>> high_card("ABCDE")
    True
    >>> high_card("AABDE")
    False
    """
    return len(set(hand)) == 5


def left_hand_stronger(first, second):
    """
    >>> left_hand_stronger("AAKQT", "AAKKT")
    False
    """
    assert first != second, "cannot have identical hands!"
    for l, r in zip(first, second):
        if l == r:
            continue
        return left_card_stronger(l, r)


tests = (
    five_of_a_kind,
    four_of_a_kind,
    full_house,
    three_of_a_kind,
    two_pairs,
    one_pair,
    high_card,
)


def get_hand_type(hand):
    global tests
    N = len(tests)
    if "J" in hand:
        best_result = 0
        for r in cards:
            if r == "J":
                continue
            fake_hand = hand.replace("J", r)
            new_result = get_hand_type(fake_hand)
            if new_result > best_result:
                best_result = new_result
                best_hand = fake_hand

        return best_result
    # no jokers present so continue
    for j, t in enumerate(tests):
        r = t(hand)
        if r:
            return N - j


def play_round(left, right):
    """
    return 1 if left player wins
    return 0 if draw
    return -1 if right player wins
    """
    ltype = get_hand_type(left)
    rtype = get_hand_type(right)
    if ltype > rtype:
        return 1
    elif ltype < rtype:
        return -1
    return left_hand_stronger(left, right)


if testing:
    import doctest

    doctest.testmod()

# Insertion Sort needed
hands = []
for row in load_data_gen(fn, testing):
    hand, bet = row.split(" ")
    hands.append((hand, bet))

# bubble sort babyee
swaps = True
while swaps:
    swaps = False
    j = 0
    while j < len(hands) - 1:
        left = hands[j][0]
        right = hands[j + 1][0]
        if play_round(left, right) == 1:
            swaps = True
            hands[j], hands[j + 1] = hands[j + 1], hands[j]
        j += 1

total = 0
for j, (hand, bet) in enumerate(hands, 1):
    print(j, hand, bet)
    total += j * int(bet)

print(f"This gives a total of {total}")
