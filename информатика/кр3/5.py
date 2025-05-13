def f(n):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = s.replace("1", "11")
    else:
        s = s.replace("0", "00")

    return int(s, 2)


for n in range(300, 0, -1):
    r = f(n)
    if (r < 70) and (n != r):
        print(n)
        break
