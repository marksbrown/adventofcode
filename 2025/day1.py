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
        if t == "L":
            dial_position = (dial_position - v) % 100
        elif t == "R":
            dial_position = (dial_position + v) % 100
        else:
            raise ("wat")

        if not dial_position:
            count += 1

print(count)
