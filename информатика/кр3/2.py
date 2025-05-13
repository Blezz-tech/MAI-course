def f(x, y, z, w):
    return (w <= (z != y)) and (z or (y <= x))


print("y x w z r")

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                r = int(f(x, y, z, w))
                if r == 0:
                    print(y, x, w, z, r)


"""

y x w z r
0 0 1 0 0
1 0 0 0 0
0 1 1 0 0

1 0 1 0 0
1 0 1 1 0
1 1 1 1 0

"""
