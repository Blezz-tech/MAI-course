def f(x):
    s = bin(x)[2:]

    s += "1" if s.count("1") > s.count("0") else "0"

    return int(s, 2)


for x in range(1, 256):
    R = f(x)
    if R > 100:
        print(R)
        break