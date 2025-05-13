def f(n):
    s = bin(n)[2:]

    if n % 2 == 0:
        s += '0'
    else:
        s += '1'

    if s.count('1') % 3 == 0:
        s = "11" + s[2:]
    else:
        s = "10" + s[2:]
    return int(s, 2)


for N in range(1000, 1, -1):
    R = f(N)
    if R <= 37:
        print(N)
        break
