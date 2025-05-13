def f(x, a):
    return ((x % 20 == 0) <= (not (x % 11 == 0))) or ((x + a) >= 300)


for A in range(1, 100):
    lst = []
    for x in range(1, 300):
        lst.append(f(x, A))

    if all(lst):
        print(A)
        break


