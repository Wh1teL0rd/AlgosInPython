def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        if not lines:
            raise ValueError("Файл порожній")

        N = int(lines[0])
        pairs = [tuple(map(int, line.split())) for line in lines[1:]]

    return N, pairs
