def converter(x):
    s = ''

    while x:
        s += str(x % 8)
        x //= 8

    return s[::-1]


x = converter(4 ** 2022 - 6 * 4 ** 522 + 5 * 64 ** 510 - 3 * 2 ** 330 - 100)

print(x.count('7'))
