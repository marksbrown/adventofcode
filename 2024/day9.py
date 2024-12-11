from itertools import pairwise
fn = "test_data"
fn = "data"

raw_data = []
with open(fn) as f:
    for row in f:
        row = row.strip('\n')
        if row:
            raw_data.append(row)

def parse(data):
    indices = []
    start = 0
    current_id = 0
    for j, sym in enumerate(data):
        if j % 2:
            lbl = "."
        else:
            lbl = current_id
            current_id += 1

        if not int(sym):
            continue
        end = start + int(sym)
        indices.append((start, end, lbl))
        start = end
    return indices

def pprint(seq, pad=0, simple=False):
    for i, j, sym in seq:
        if simple:
            if sym == ".":
                print(str(sym)*(j-i), end="")
            else:
                print("#"*(j-i), end="")
        else:
            print(str(sym)*(j-i), end="")
    print("."*pad, end="")
    print("")

def is_contiguous(indices) -> bool:
    for start, end, file_id in indices:
        if file_id == ".":
            return False
    return True
   
def checksum(indices):
    t = 0
    for i, j, file_id in indices:
        if file_id == ".":
            continue
        for v in range(i, j):
            t += v * file_id
    return t

for row in raw_data:
    print("=", row, "=")
    indices = parse(row)
    total_memory = indices[-1][1]
    print(f"Memory addresses available: {total_memory}")
    k = 0
    place_group = len(indices) - 1
    while not is_contiguous(indices) and place_group > 0:
        if fn == "test_data":
            pprint(indices, pad=total_memory - indices[-1][1])
        else:
            print(f"{total_memory - place_group}/{total_memory}")
        if indices[place_group][2] == ".":
            place_group -= 1
            continue
        i, j, file_id = indices[place_group]
        file_size = j - i
        for k in range(place_group):
            if indices[k][-1] != ".":  # keep going until we find an empty group
                k += 1
                continue
            x, y, _ = indices[k]
            gap_size = y - x
            if gap_size == file_size:  # perfectly matched
                indices[k] = (x, y, file_id)
                indices[place_group] = (i, j, ".")
                break
            elif gap_size > file_size:  # gap is larger than group to be placed
                indices[k] = (x, x + file_size, file_id)
                indices[place_group] = (i, j, ".")
                indices.insert(k+1, (x + file_size, y, '.'))
                place_group += 1
                break
            
        place_group -= 1
    pprint(indices, pad=total_memory - indices[-1][1])
    print(f"The checksum is {checksum(indices)}")

# part A version
# for row in raw_data:
#     print("=", row, "=")
#     indices = parse(row)
#     total_memory = indices[-1][1]
#     print(f"Memory addresses available: {total_memory}")
#     k = 0
#     while not is_contiguous(indices):
#         if fn == "test_data":
#             pprint(indices, pad=total_memory - indices[-1][1])
#         i, j, file_id = indices.pop()
#         if file_id == ".":
#             continue
#         file_size = j - i
#         while k < len(indices):
#             if indices[k][-1] != ".":  # keep going until we find an empty group
#                 k += 1
#                 continue
#             x, y, _ = indices[k]
#             gap_size = y - x
#             if gap_size == file_size:  # perfectly matched
#                 indices[k] = (x, y, file_id)
#                 file_size = 0
#             elif gap_size > file_size:  # gap is larger than group to be placed
#                 indices[k] = (x, x + file_size, file_id)
#                 indices.insert(k+1, (x + file_size, y, '.'))
#                 file_size = 0
#             else:  # block size is larger than gap size
#                 indices[k] = (x, y, file_id)
#                 file_size -= gap_size

#             if not file_size:
#                 break
#         else:  # leftover
#             indices.append((i, i+file_size, file_id))
#     pprint(indices, pad=total_memory - indices[-1][1])
#     print(f"The checksum is {checksum(indices)}")
