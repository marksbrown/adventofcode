from os.path import join

def load_data_gen(fn):
    with open(join("data", fn), 'r') as f:
        for row in f:
            row = row.strip('\n')
            yield row
