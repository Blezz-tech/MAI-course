def f(x, y, z, w):
    return not (not x or y) or not (z or w) or z


for x1 in range(0, 2):
    for y1 in range(0, 2):
        for z1 in range(0, 2):
            for w1 in range(0, 2):
                result = f(x1, y1, z1, w1)
                if not result:
                    print(x1, w1, y1, z1, 1 if result else 0)

# 1 1 1 0 0
# 0 1 1 0 0
# 0 1 0 0 0