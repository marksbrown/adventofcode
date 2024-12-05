fn = "test_data"
fn = "data"
former = True

a_before_b = {}
updates = []

with open(fn) as f:
    for row in f:
        row = row.strip('\n')
        if not row:
            former = False
            continue
        if former:
            a, b = row.split('|')
            a = int(a)
            b = int(b)
            if a in a_before_b:
                a_before_b[a].append(b)
            else:
                a_before_b[a] = [b,]
        else:
            updates.append([int(v) for v in row.split(',') if v])


def ppdict(dict_):
    for k in sorted(dict_):
        print(k, ":", dict_[k])

print("Before")
ppdict(a_before_b)
print("")

def valid_position(v, seq) -> bool:
    """
    Determines if :v: obeys rules outlined in :a_before_b:
    in :seq:
    """
    if v not in a_before_b:
        return True 

    for after in a_before_b[v]:
        if after not in seq:
            continue
        if seq.index(after) < seq.index(v):
            return False

    return True

total = 0
total_changed = 0
N = 100  # brute force my unreliable sort!
for update in updates:
    update_sorted = sorted(update, key = lambda k : valid_position(k, update))
    for _ in range(N):
        update_sorted = sorted(update_sorted, key = lambda k : valid_position(k, update_sorted))
    

    if update_sorted == update:
        total += update_sorted[len(update) // 2]
    else:
        print(update, "->", update_sorted)
        total_changed += update_sorted[len(update) // 2]

print(f"Total for part a is", total)
print(f"Total for part b is", total_changed)

