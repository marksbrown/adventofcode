from useful import load_data_gen
import turtle as tl
from time import sleep
from itertools import zip_longest
from math import sqrt

tl.tracer(0, 0)
tl.hideturtle()

fn = "day6"
testing = False
verbose = False


def goto(t, pos):
    tl.penup()
    t.goto(*pos)
    tl.pendown()


def motion(initpos, acceleration, start_at, finish_line, delta=1, **kwargs):
    x, y = initpos
    speed = start_at * acceleration
    time = 0
    while x < finish_line:
        if time >= start_at:
            x = speed * time
            yield x, y
        time += delta


class Vector1D:
    """
    Lazy implementation of vectors

    >>> Vector1D(1,2)
    [1, 2]
    """

    def __init__(self, *vec):
        self._vec = [int(x) for x in vec]

    def __len__(self):
        return len(self._vec)

    def __abs__(self):
        return sqrt(map(lambda x: x * x, self))

    def __str__(self):
        return f"[{', '.join(map(str, self._vec))}]"

    def __iter__(self):
        yield from self._vec

    def __repr__(self):
        return self._vec

    def __add__(self, other):
        if isinstance(other, Vector1D):
            return Vector1D(*[x + y for x, y in zip_longest(self, other, fillvalue=0)])
        return Vector1D(*[x + other for x in self])

    def __mul__(self, other):
        if isinstance(other, Vector1D):
            raise NotImplementedError("Don't you go getting fancy on me")
        r = Vector1D(*[x * other for x in self])
        return r

    def __rmul__(self, other):
        return self.__mul__(other)

    def __getitem__(self, key):
        return self._vec[key]


test_vec = False
if test_vec:
    x = Vector1D(2, 1)
    y = Vector1D(2, 2)
    print(x, y)
    print(x + y)
    print(x * 2)
    print(y * 0)
    print("Trying bad operations")
    try:
        r = y + 3
    except TypeError:
        r = "Undefined"
    print(r)

    try:
        r = 3 + y
    except TypeError:
        r = "Undefined"
    print(r)


class Runner:
    def __init__(self, initpos, go_at, acceleration, **kwargs):
        self.initpos = initpos
        self.pos = initpos
        self.go_at = go_at
        self.v = go_at * acceleration
        self.t = tl.Turtle()
        self.time = kwargs.get("initial_time", 0)
        self.jump()  # go to initial position!

    def jump(self):
        tl.penup()
        self.t.goto(*self.pos)
        tl.pendown()

    def step(self, delta):
        self.time += delta
        if self.time >= self.go_at:
            self.pos = self.v * (self.time - self.go_at) + self.initpos

    def walk(self):
        self.t.goto(*self.pos)


def get_winning_moves(best_distance, race_duration, **kwargs):
    acceleration = kwargs.get("acceleration", Vector1D(1, 0))
    finish_line = kwargs.get("finish_line", 1000)  # Ideally not reached!
    delta = kwargs.get("delta", 0.1)
    real_time = kwargs.get("real_time", False)

    num_of_turtles = race_duration
    initial_positions = map(lambda y: Vector1D(0, y * 10), range(num_of_turtles + 1))
    runners = [Runner(pos, j, acceleration) for j, pos in enumerate(initial_positions)]

    time = 0
    race_finished = False
    while not race_finished:
        surviving_runners = []
        for runner in runners:
            runner.walk()
            if time > race_duration:
                if verbose:
                    print("Race Over!")
                race_finished = True
                break
            runner.step(delta)

        tl.update()
        if real_time:
            sleep(delta)
        time += delta

    runners = sorted(runners, key=lambda r: runner.pos[0])
    total = 0
    for rid, runner in enumerate(runners, 1):
        dist = runner.pos[0]
        if verbose:
            print(f"Runner {rid} finishes at {dist:.1f} m ")
        if dist > best_distance:
            if verbose:
                print(f"This result beats best distance by {dist - best_distance}")
            total += 1

    return total


import re


def load_data():
    for row in load_data_gen(fn, testing):
        row = row.strip("\n")
        name, values = row.split(":")
        values = values.rstrip(" ").lstrip(" ")
        values = [int(x) for x in values.split(" ") if x]
        yield name, values


raw = {k: v for k, v in load_data()}

data = []
for k in raw:
    data.append(raw[k])

result = 1
for time, dist in zip(*data):
    r = get_winning_moves(dist, time)
    result *= r

print(result)
tl.exitonclick()
