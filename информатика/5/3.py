def f(x):
    s = bin(x)[2:]

    s += "01" if x % 2 == 0 else "10"

    return int(s, 2)


for x in range(1, 256):
    R = f(x)
    if R > 62:
        print(R)
        break