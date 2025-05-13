def f(n):
    s = bin(n)[2:]

    if n % 4 == 0:
        s += s
    else:
        s += s[::-1]

    return int(s, 2)


for i in range(1, 300):
    r = f(i)
    if r >= 544:
        print(i)
        break
