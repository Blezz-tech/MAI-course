def f(x):
    s = bin(x)[2:]

    s = "10" + s if x % 2 == 0 else "1" + s + "00"

    return int(s, 2)


numbers = []
for x in range(1, 12+1):
    R = f(x)
    numbers.append(R)

print(max(numbers))
