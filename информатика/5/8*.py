def f(x):
    x1 = x

    if x % 2 == 0:
        m = x1.bit_length()
        x1 = x1 + 2**m + 2**(m+1)
        # s = "11" + s
    else:
        x1 = (x1 << 2) + 1 * 2**1 + 0 * 2**0
        m = x1.bit_length()
        x1 = x1 + 2**m
        # s = "1" + s + "10"
    return x1


max_number = f(234567890)
for x in range(234567890+1, 567891234+1):
    max_number = max(max_number, f(x))
print(max_number)
