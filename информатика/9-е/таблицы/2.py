count = 0
for s in open('2.csv'):
    M = [int(x) for x in s.split(",")]

    v1 = len(M) != len(set(M))

    nechet = [x for x in M if x % 2 != 0]
    v2 = len(nechet) == 3

    if v1 != v2:
        count += 1

print(count)