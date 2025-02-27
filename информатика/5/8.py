def f(x):
    s = bin(x)[2:]

    s = "11" + s if x % 2 == 0 else "1" + s + "10"

    return int(s, 2)


max_number = f(234567890)
for x in range(234567890+1, 567891234+1):
    max_number = max(max_number, f(x))
print(max_number)
