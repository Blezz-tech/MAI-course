def f(x):
    s = bin(x)[2:]

    s = s[:-1]

    s += "10" if x % 2 == 1 else "01"

    return int(s, 2)


for x in range(3, 256):
    R = f(x)
    if R == 385:
        print(x)
        break
#
# for n in range(1, 256):
#
#     s = bin(n)[2:]
#
#     s = s[:-1]
#
#     s += "10" if n % 2 == 1 else "01"
#
#     R = int(s, 2)
#
#     if R == 385:
#         print(x)
#         break
