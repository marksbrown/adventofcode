from useful import load_data_gen
from string import ascii_lowercase

testing = False
test_data = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
fn = "day1"

if testing:
    data = test_data
else:
    data = load_data_gen(fn)

result = 0
for r in data:
    values = list(filter(lambda x :x not in ascii_lowercase, r))
    value = int(values[0] + values[-1])
    result += int(value)

print(result)
