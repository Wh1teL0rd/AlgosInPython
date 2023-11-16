def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline())
        pairs = [tuple(map(int, line.split())) for line in file.readlines()]
    return N, pairs