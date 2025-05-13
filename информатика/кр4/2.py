def f(x, y, z, w):
    return int(x and (z <= w) and (not y))


lst = []


for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                r = f(x, y, z, w)
                if r == 1:
                    lst.append([x, y, z, w, r])

print("x w z y r")
for line in lst:
    x, y, z, w, r = line[0], line[1], line[2], line[3], line[4]
    print(x, w, z, y, r)

# x w z y r
# 1 1 1 0 1
# 1 1 0 0 1
# 1 0 0 0 1
