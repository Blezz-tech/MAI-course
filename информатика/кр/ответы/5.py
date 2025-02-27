def f(n):
    s = bin(n)[2:]

    if n // 4 == 0:
        s += s[-1:]
    else:
        s += bin(n % 4)[2:]

    return int(s, 2)

for x in range(1000, 0, -1):
    R = f(x)
    if R < 125:
        print('x:', x, 'r:', R)
        break
