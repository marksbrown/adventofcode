#part A
fn = "test_data"
fn = "data"
word = "XMAS"

data = []
with open(fn) as f:
    for row in f:
        data.append(row.strip("\n"))

DIM = len(data)
# Iterators yield sequences seperated by "_"

def iterate_vertically(arr):
    for j in range(DIM):
        for i in range(DIM):
            yield arr[i][j]
        yield "_"


def iterate_horizontal(arr):
    for i in range(DIM):
        for j in range(DIM):
            yield arr[i][j]
        yield "_"


def iterate_diagonal(arr):
    # top-left to bottom-right
    for k in range(-DIM, DIM + 1):
        for j in range(DIM):
            i = k + j
            if 0 <= i < DIM:
                yield arr[j][i]
        yield "_"
    # top-right to bottom-left
    for k in range(2 * DIM + 1, 0, -1):
        for j in range(DIM):
            i = k - j
            if 0 <= i < DIM:
                yield arr[j][i]
        yield "_"


def seq(iterator, N):
    """
    yields strings of length :N:
    from iterator
    """
    def reset():
        return [next(iterator, None) for _ in range(N)]

    r = reset()
    while None not in r:
        R = "".join(r)

        yield R
        yield R[::-1]  # check reversed as well!
        r.pop(0)
        r.append(next(iterator, None))


count = 0
iterators = (iterate_horizontal(data),
             iterate_vertically(data), 
             iterate_diagonal(data))

total = 0
for iter_ in iterators:
    count = 0
    for p in seq(iter_, len(word)):
        if p == word:
            count += 1
    print(iter_.__name__, count)
    total += count

print(f"'{word}' has been found {total} times")


# part B : x-mas problem (completely different)
# search for MAS!
def pattern_found(arr, i, j) -> bool:
    if (
        arr[i - 1][j - 1] == "M"
        and arr[i + 1][j + 1] == "S"
        or arr[i - 1][j - 1] == "S"
        and arr[i + 1][j + 1] == "M"
    ):
        if (
            arr[i + 1][j - 1] == "M"
            and arr[i - 1][j + 1] == "S"
            or arr[i + 1][j - 1] == "S"
            and arr[i - 1][j + 1] == "M"
        ):
            return True
    else:
        return False


count = 0
for i in range(1, DIM - 1):
    for j in range(1, DIM - 1):
        if data[i][j] == "A":
            try:
                r = pattern_found(data, i, j)
            except IndexError:
                continue
            if r:
                count += 1

print("Part B (fuck you) results in", count)
