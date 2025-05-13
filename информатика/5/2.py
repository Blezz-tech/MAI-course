def f(x):
    s = bin(x)[2:]

    s += s[-1:]

    s += "0" if s.count("1") % 2 == 0 else "1"

    s += "0" if s.count("1") % 2 == 0 else "1"

    return int(s, 2)

for x in range(1, 256):
    result = f(x)
    if result > 160:
        print(x)
        break
