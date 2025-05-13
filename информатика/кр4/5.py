def f(n):
    s = bin(n)[2:]

    if s.count('1') % 2 == 0:
        s += '0'
        s = '10' + s[2:]
    else:
        s += '1'
        s = '11' + s[2:]

    return int(s, 2)

for n in range(1, 1000):
    r = f(n)
    if r > 480:
        print(n)
        break
