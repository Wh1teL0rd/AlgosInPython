def count_of_pairs(pairs):
    tribes = [set(pairs[0])]
    count = 0

    for pair in pairs[1:]:
        for tribe in tribes:
            if any(person in tribe for person in pair):
                tribe.update(pair)
                break
            else:
                tribes.append(set(pair))

    for i in range(len(tribes)):
        for j in range(i+1, len(tribes)):
            for first_person in tribes[i]:
                for second_person in tribes[j]:
                    if first_person % 2 != second_person % 2:
                        count += 1

    return count
