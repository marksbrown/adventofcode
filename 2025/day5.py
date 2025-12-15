import heapq
from itertools import pairwise

testing = False

if testing:
    fn = "data/test_data"
else:
    fn = "data/day5"


class Interval:
    pass


class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __lt__(self, other):
        return self.low + other.high < other.low + other.high

    def __repr__(self):
        return f"{self.low}-{self.high}"

    def get_cases(self, other):
        return (
            other.low <= self.low <= other.high,
            other.low <= self.high <= other.high,
            self.low <= other.low <= self.high,
            self.low <= other.high <= self.high,
        )

    def contains(self, value):
        return self.low <= value <= self.high

    def union(self, other) -> Interval:
        cases = self.get_cases(other)
        if not any(cases):
            return self
        values = sorted((self.low, self.high, other.low, other.high))
        return Interval(values[0], values[-1])

    def any_overlap(self, other) -> bool:
        cases = self.get_cases(other)
        return any(cases)

    def is_subset(self, other) -> bool:
        cases = self.get_cases(other)
        return all(cases[-2:])

    def total(self) -> int:
        return self.high - self.low + 1


ranges = []
ids = []
first = True
with open(fn) as f:
    for line in f:
        line = line.strip("\n")
        if not line:
            first = False
            continue

        if first:
            ranges.append(list(map(lambda x: int(x), line.split("-"))))
        else:
            ids.append(line)


def union_intervals(intervals):
    for j, left in enumerate(intervals):
        for right in intervals:
            if left == right:
                continue

            if left.any_overlap(right):
                new_interval = left.union(right)
                intervals[j] = new_interval
                intervals.pop(intervals.index(right))
                return True, intervals

    return False, intervals


for j, r in enumerate(ranges):
    if not j:
        intervals = [
            Interval(*r),
        ]
        heapq.heapify(intervals)
        continue

    interval = Interval(*r)
    heapq.heappush(intervals, interval)

modified = True
while modified:
    modified, intervals = union_intervals(intervals)

print(*sorted(intervals), sep="\n")


def check_intervals(intervals, value):
    for interval in intervals:
        if interval.contains(value):
            return True
    return False


## part A
fresh = sum((check_intervals(intervals, int(i)) for i in ids))
print(f"There are {fresh} fresh ingredients")

## part B
count_fresh = sum((interval.total() for interval in intervals))
print(f"There are {count_fresh} total fresh ingredients available")
