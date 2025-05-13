lines = open('9.csv').read().split('\n')
lines = list(map(
    lambda x: list(map(int, x.split(','))),
    lines
))

count = 0
for line in lines:
    [a, b, c, d] = line

    v1 = len(set(line)) == 3

    [x1, x2] = sorted(line)[1:-1]

    v2 = x1 > 23 and x2 > 23
    if v1 and v2:
        count += 1

print(count)
