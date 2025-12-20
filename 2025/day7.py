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
        print(current_state)
        self.current_state = [1 if elem == "|" else 0 for elem in current_state]
        self.obstacles = obstacles
        self.current_y = 0

    @property
    def count(self):
        return sum(self.current_state[j] for j in range(self.width))

    @property
    def width(self):
        return len(self.current_state)

    def collision(self, x):
        if self.current_y + 1 < dims[1]:
            return x in self.obstacles[self.current_y + 1]
        else:
            return False

    def step(self):
        collisions = [
            j
            for j, active in enumerate(self.current_state)
            if active and self.collision(j)
        ]

        for j in collisions:
            if j > 1:
                self.current_state[j - 1] += self.current_state[j]
            if j < self.width:
                self.current_state[j + 1] += self.current_state[j]
            self.current_state[j] = 0

        self.current_y += 1

    def __repr__(self):
        r = [str(elem).zfill(2) for elem in self.current_state]
        r = [elem if elem[-1] != "0" else "  " for elem in r]
        for obstacle in self.obstacles.get(self.current_y, []):
            r[obstacle] = "^^"
        return str(r)


t = Tachyon(start_line, obstacles)
for i in range(dims[1] + 1):
    print(f"{i:2}", "::", t, "::", t.count)
    t.step()
