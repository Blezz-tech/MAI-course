
for x in range(0, 20):
    a = 8 * 21 ** 6 + \
        2 * 21 ** 5 + \
        9 * 21 ** 4 + \
        3 * 21 ** 3 + \
        4 * 21 ** 2 + \
        x * 21 ** 1 + \
        2 * 21 ** 0
    b = 2 * 21 ** 6 + \
        9 * 21 ** 5 + \
        2 * 21 ** 4 + \
        4 * 21 ** 3 + \
        x * 21 ** 2 + \
        x * 21 ** 1 + \
        7 * 21 ** 0
    c = 6 * 21 ** 6 + \
        7 * 21 ** 5 + \
        5 * 21 ** 4 + \
        6 * 21 ** 3 + \
        4 * 21 ** 2 + \
        x * 21 ** 1 + \
        8 * 21 ** 0

    R = a + b + c
    if R % 20 == 0:
        print(R / 20)
        break
