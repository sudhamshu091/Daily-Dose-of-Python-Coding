import itertools
sequence = [22, 12, 18, 87, 88, 17, 9, 25, 10, 24, 89, 16, 19, 86, 23, 11]
for i in range(len(sequence)):
    for j in itertools.combinations(sequence, i):
        if len(j) == 4:
            if sum(j) == 139:
                print(j)
