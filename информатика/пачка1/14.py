def converter(x):
    s = ""

    while x:
        s += str(x % 6)
        x //= 6

    return s[::-1]


for x in range(1000, 0, -1):
    i = 6**2025 + 6**25 - x
    r = converter(i)
    if r.count("0") == 2002:
        print(x)
        break
