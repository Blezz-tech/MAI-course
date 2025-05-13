lst = open('9.csv').read().split('\n')
lst = [[int(x) for x in line.split(',')] for line in lst]

count = 0

for line in lst:
    a, b, c, d, e, f, g = line

    lst_set = set(line)

    v0 = len(lst_set) == 3
    v1 = True

    if v0 and v1:
        print(sorted(line))
        count += 1

print(count)

# [23, 23, 38, 38, 38, 38, 46]-
# [64, 64, 64, 86, 86, 86, 97]-
# [1, 1, 1, 2, 94, 94, 94]+
