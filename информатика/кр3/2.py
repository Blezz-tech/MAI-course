def f(x, y, z, w):
    return int(y and (x <= w) and ((not x) <= ((not w) == z)))


lst = []

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                r = f(x, y, z, w)
                lst.append((x, y, z, w, r))

lst_sorted = sorted(lst, key=lambda x: x[4])


print("x z y w r")
for line in lst_sorted:
    (x, y, z, w, r) = line
    print(x, z, y, w, r)

# x z y w r
# 0 0 1 1 1
# 0 1 1 0 1
# 1 1 1 0 0

