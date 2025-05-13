def f(x, A):
    return ((x % 14 == 0) <= (x % 4 != 0)) or (x + A >= 200)


for A in range(1, 300):
    if all([f(x, A) for x in range(1, 300)]):
        print(A)
        break
