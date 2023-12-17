from useful import load_data_gen
import turtle as tl
from time import sleep
from itertools import zip_longest
from math import sqrt, gcd, floor

tl.tracer(0, 0)
tl.hideturtle()

fn = "day6"
testing = False
verbose = True


def ceiling(v):
    """
    >>> ceiling(14.2)
    15
    >>> ceiling(14.0001)
    15
    >>> ceiling(14.999)
    15
    """
    if v > floor(v):
        return floor(v) + 1
    else:
        return floor(v)


import doctest

doctest.testmod()


def actual_solve(d, T):
    """
    Of course this is a trivial physics problem so let's just solve it that way
    """
    dt = sqrt(T**2 - 4 * d)
    t2 = (T + dt) / 2
    t1 = (T - dt) / 2
    return t1, t2


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


partA = False
raw = {k: v for k, v in load_data()}

data = []
if partA:
    for k in raw:
        data.append(raw[k])
else:
    actual_time = int("".join(map(str, raw["Time"])))
    actual_dist = int("".join(map(str, raw["Distance"])))
    data.append(
        [
            actual_time,
        ]
    )
    data.append(
        [
            actual_dist,
        ]
    )


result = 1
easier_result = 1
skip_old_method = True
for time, dist in zip(*data):
    print(time, dist)
    if not skip_old_method:
        r = get_winning_moves(dist, time)
        print(f"Brute force solution is {r}")
        result *= r
    t1, t2 = actual_solve(dist, time)
    print(f"Analytical solution provides {t1} and {t2}")
    w_high = ceiling(t2) - floor(t1)
    w_low = floor(t2) - ceiling(t1)
    print(f"Giving a possible range of {w_low} to {w_high}")
    if w_low == w_high:
        w = w_low - 1
    else:
        w = (w_low + w_high) // 2
    easier_result *= w

print(result, easier_result)
if not skip_old_method:
    tl.exitonclick()
