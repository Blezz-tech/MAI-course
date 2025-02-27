def f(x):
    s = bin(x)[2:]

    s += str(s.count("1") % 2)

    s += str(s.count("1") % 2)

    return int(s, 2)

for x in range(1, 256):
    R = f(x)
    if R > 85:
        print(x)
        break