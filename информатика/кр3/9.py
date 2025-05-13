lst = open('9.csv').read().split('\n')
lst = [list(map(int, item.split(','))) for item in lst]

count = 0

for line in lst:

    line = sorted(line)
    v0 = (sum(line[1:]) / 5) > line[0]
    v1 = line[0] * line[3] == line[1] * line[2]

    if v0 and v1:
        count += 1

print(count)