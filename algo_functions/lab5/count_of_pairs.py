def count_of_pairs(pairs):
    boy_set = set()
    girl_set = set()

    for pair in pairs:
        boy, girl = pair
        if boy % 2 == 1:
            boy_set.add(boy)
        if girl % 2 == 0:
            girl_set.add(girl)

    possible_pairs = len(boy_set) * len(girl_set)

    return possible_pairs
