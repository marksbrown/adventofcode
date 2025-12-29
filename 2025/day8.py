from scipy.spatial import KDTree

testing = True 

if testing:
    fn = "data/test_data"
else:
    fn = "data/day8"


data = []
with open(fn) as f:
    for row in f:
        row = row.strip('\n')
        data.append(tuple(map(int,row.split(','))))
        print(row)

print("==")

pairs = {}
tree = KDTree(data)
for k, node in enumerate(data):
    _, indices = tree.query(node, k=3)
    print(k, indices)

