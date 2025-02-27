def f(s):
    while "13" in s or "233" in s or "333" in s:
        if "13" in s:
            s = s.replace('13', '21', 1)
        if "233" in s:
            s = s.replace('233', '13', 1)
        if "333" in s:
            s = s.replace('333', '2', 1)
    return int(s)

count = 0
for n in range(3, 4001):
    if f("2" + str(n)):
        count += 1
print(count)