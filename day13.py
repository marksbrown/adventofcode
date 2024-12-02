from useful import load_data_gen

fn = "day13"
testing = False

def load_pattern():
    data = []
    for row in load_data_gen(fn, testing):
        if row == "=":
            yield data
            data = []
        else:
            data.append([1 if itm == "#" else 0 for itm in row])
    if data:
        yield data

def transpose(arr):
    return list(zip(*arr))

def count_apart(i, j):
    yield from zip(range(i, -1, -1), range(i+1, j))

def is_mirror(arr, i):
    """
    Check if all rows specified by
    (i and i+1), (i-1, i+2), (i-2, i+3), ..
    match
    """
    to_check = tuple(count_apart(i, len(arr)))
    if all(arr[x] == arr[y] for x,y in to_check) and to_check:
        return True
    else:
        return False

t = 0
lbl = ("row", "col")
for pat in load_pattern():
    print(*pat, sep="\n")
    for i, arr in enumerate((pat, transpose(pat))):
        for j in range(len(arr[0])+1):
            if is_mirror(arr, j):
                if not i:
                    v = (j + 1) * 100
                else:
                    v = j + 1
                print(lbl[i], j+1, "adds", v)
                t += v

print(f"The total is {t}")
