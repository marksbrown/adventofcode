import re
from itertools import product 
fn = "test_data"
fn = "data"

rows = []
with open(fn) as f:
    for row in f:
        row = row.strip('\n')
        v, values = row.split(':')
        v = int(v)
        numbers = []
        for value in values.split(' '):
            if not value:
                continue
            numbers.append(int(value))

        rows.append((v, numbers))

def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "|":
        return int(str(a) + str(b))
    else:
        raise NotImplementedError("wat")

def calculate(seq):
    while len(seq) > 1:
        a = seq.pop(0)
        b = seq.pop(0)
        op = seq.pop(0)
        seq.insert(0, calc(a,b,op))
    return seq[0]

valid_operators = "+*|"
bestest_values = []
for v, values in rows:
    for operators in product(valid_operators, repeat=len(values) - 1):
        t = values[:]
        operators = list(operators)
        r = [t.pop(0), t.pop(0), operators.pop(0)]
        for op in operators:
            r.append(t.pop(0))
            r.append(op)
        result = calculate(r[:])
        if v == calculate(r[:]):
            if v not in bestest_values:
                bestest_values.append(v)

print(f"The total is {sum(bestest_values)}")

    

