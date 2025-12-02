import common as cm

testing = False

if testing:
    fn = "data/test_data"
else:
    fn = "data/day1"


def parse(line):
    line = line.strip("\n")
    turn = line[0]
    value = int(line[1:])
    return turn, value


dial_position = 50  # initial
count = 0
with open(fn) as f:
    for line in f:
        t, v = parse(line)
        turns, v = divmod(v, 100)
        count += turns
        if t == "L":
            new_dial_position = dial_position - v
        elif t == "R":
            new_dial_position = dial_position + v
        else:
            raise ("wat")

        # count passing zero, not landing on it
        # case 1 - pass 0 to the left
        alt = False
        if new_dial_position <= 0 and dial_position > 0:
            alt = True

        # case 2 - pass 0 to the right
        if new_dial_position >= 100:
            alt = True

        dial_position = new_dial_position % 100
        if alt:
            count += 1

print(count)
