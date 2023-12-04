from os.path import join


def load_data_gen(fn, testing=False):
    if testing:
        x = open("test_data", "r")
    else:
        x = open(join("data", fn), "r")
    with x as f:
        for row in f:
            row = row.strip("\n")
            yield row
