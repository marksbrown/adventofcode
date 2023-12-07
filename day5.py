from useful import load_data_gen
import re

pat = re.compile("(\w+)\-to\-(\w+)\smap")
fn = "day5"
testing = False


def parse_row(row):
    values = row.split(" ")
    assert len(values) == 3, "errr"
    l, c, r = map(int, values)
    return (l, l + r), (c, c + r)


data = {}
for j, row in enumerate(load_data_gen(fn, testing)):
    if not j:
        seeds = [int(v) for v in row.split(":")[1].split(" ") if v]
        data["seeds"] = seeds
        continue
    if ":" in row:
        x = re.findall(pat, row)[0]
        f, t = x
        data[f] = {t: {}}
    else:
        destination, source = parse_row(row)
        if data[f][t]:
            data[f][t]["source"].append(source)
            data[f][t]["destination"].append(destination)
        else:
            data[f][t] = {
                "source": [
                    source,
                ],
                "destination": [
                    destination,
                ],
            }


def shift(v, left, right):
    low, _ = left
    return right[0] + (v - low)


# any source not found in their respective map doesn't change
results = {}
for seed in data["seeds"]:
    maxruns = 100
    if testing:
        print(f"seed number {seed}")
    current = "seed"
    value = seed
    while current != "location":
        for dest in data[current]:
            if testing:
                print(f"{current} -> {dest}")
                print(f"{current} number corresponds to ", end="")
            for j, src in enumerate(data[current][dest]["source"]):
                low, high = src
                if low <= value <= high:
                    destination = data[current][dest]["destination"][j]
                    value = shift(value, src, destination)
                    break
            current = dest
            if testing:
                print(f"{current} number {value}")
            break
    results[seed] = value

for seed in sorted(results, key=lambda k: results[k]):
    print(f"{seed} seed has a location value of {results[seed]} location number")
