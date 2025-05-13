def f(x, A):
    return ((x % 9 == 0) <= (x % 6 != 0)) or (x + A >= 100)


for A in range(1, 300):
    if all([f(x, A) for x in range(1, 300)]):
        print(A)
        break
