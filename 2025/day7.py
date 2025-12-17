testing = False

if testing:
    fn = "data/test_data"
else:
    fn = "data/day7"


obstacles = {}

with open(fn) as f:
    for j, line in enumerate(f):
        line = line.strip("\n")
        if "S" in line:
            start_line = line.replace("S", "|").replace(".", "0")
        else:
            obstacles[j] = [i for i, sym in enumerate(line) if sym == "^"]

dims = (len(line), j)


class Tachyon:
    def __init__(self, current_state, obstacles):
        self.current_state = current_state
        self.obstacles = obstacles
        self.current_y = 0
        self.count = 0

    @property
    def width(self):
        return len(self.current_state)

    def collision(self, x):
        return x in self.obstacles[self.current_y + 1]

    def split(self, x):
        pass

    def step(self):
        if self.current_y >= dims[1]:
            return 0

        next_state = [
            0,
        ] * self.width
        for j, current in enumerate(self.current_state):
            if current == "|":
                if self.collision(j):
                    self.count += 1
                    if j > 0:
                        next_state[j - 1] = "|"
                    if j < self.width:
                        next_state[j + 1] = "|"
                else:
                    next_state[j] = current

        self.current_y += 1
        self.current_state = next_state

    def __repr__(self):
        str_state = list(self.current_state)
        for obstacle in self.obstacles.get(self.current_y, []):
            str_state[obstacle] = "^"
        return "".join(map(str, str_state))


t = Tachyon(start_line, obstacles)
for i in range(dims[1] + 5):
    print(f"{i:2}", "::", t, "::", t.count)
    t.step()
