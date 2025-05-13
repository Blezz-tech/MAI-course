def f(x, y, z, w):
    return int((not (x <= y)) or ((not z) == (w <= x)) or w)


print("w z x y r")


for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                r = f(x, y, z, w)
                if r == 0:
                    print(w, z, x, y, r)
