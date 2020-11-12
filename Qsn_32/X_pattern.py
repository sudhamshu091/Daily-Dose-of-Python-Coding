n = 3
for i in range(-n, n + 1):
    print('{}*{}{}'.format((n + 1 - abs(i)) * ' ',(2 * abs(i) - 1) * ' ','' if i == 0 else '*'))
