f = open('9.csv').readlines()
lst = [[int(x) for x in line.split(',')] for line in f]

count = 0
for line in lst:
    a, b, c, d = line[0], line[1], line[2], line[3]

    line.sort()

    v1 = line[-1] > sum(line[:-1])
    v2 = a != b and a != c and a != d and b != c and b != d and c != d
    if v1 and v2:
        count += 1


print(count)