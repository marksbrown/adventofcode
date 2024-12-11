from functools import cache
import doctest

fn = "test_data"
fn = "data"

@cache
def transform(v : int):
    """
    >>> transform(0)
    (1, None)
    >>> transform(20)
    (2, 0)
    >>> transform(1)
    (2024, None)
    """
    if not v:
        return 1, None
    elif not len(str(v)) % 2:
        sv = str(v)
        mid = len(sv) // 2
        return int(sv[:mid]), int(sv[mid:])
    else:
        return v * 2024, None

if fn == "test_data":
    doctest.testmod()

values = {}
with open(fn) as f:
    for line in f:
        line = line.strip('\n')
        for j, v in enumerate(line.split(' ')):
            v = int(v)
            if v not in values:
                values[v] = 1
            else:
                values[v] += 1

def evolve(values):
    r = {}
    for v in values:
        f, s = transform(v)
        if f in r:
            r[f] += values[v]
        else:
            r[f] = values[v]
        if s is not None:
            if s in r:
                r[s] += values[v]
            else:
                r[s] = values[v]
    return r
        

    return values

evolutions = 75
for j in range(evolutions):
    values = evolve(values)
    print(f"After {j+1} blinks")
    print(values)

for v in sorted(values, key = lambda k : values[k]):
    print(v, end=" ")

print("")
total = sum(values[v] for v in values)
print(f"After {evolutions} evolutions you have {total} stones")

