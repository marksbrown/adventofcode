import numpy as np
import re
fn = "test_data"
fn = "data"

to_parse = []
with open(fn) as f:
    for row in f:
        row = row.strip('\n')
        if not row:
            continue
        to_parse.append(row)

cost = np.array([3,1]).T  # 1 token for button a and 3 tokens for button b

tokens = 0
for j in range(0, len(to_parse), 3):
    print(j // 3 + 1)
    button_a = to_parse[j].split(':')[-1]
    button_b = to_parse[j+1].split(':')[-1]
    prize = to_parse[j+2].split(':')[-1]
    new_machine = {}
    for lbl, d in (('a', button_a), ('b', button_b), ('r', prize)):
        new_machine[lbl] = tuple(map(int,re.findall('([0-9]+)', d)))

    new_machine['r'] += np.array([10000000000000, 10000000000000])
    new_machine['A'] = np.array([new_machine['a'], new_machine['b']]).T
    new_machine['invA'] = np.linalg.inv(new_machine['A'])
    new_machine['soln'] = new_machine['invA'].dot(new_machine['r'])

    if all(round(v,3).is_integer() for v in new_machine['soln']):
        print(new_machine['soln'])
        r = new_machine['soln'].dot(cost)
        r = np.sum(np.round(r,3))
        print(r)
        tokens += r

print(f"Total tokens used", tokens)



