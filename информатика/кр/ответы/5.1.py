def f(n):
    s = bin(n)[2:]

    if n // 2 == 0:
        s = '11' + s
    else:
        s = '1' + s + '10'
    return int(s, 2)


x_max = f(234567890)
for x in range(234567890, 567891234 + 1):
    x_max = max(x_max, f(x))
print(x_max)