count = 0
for s in open('1.csv'):
    M = [int(x) for x in s.split(",")]
    if len(M) == len(set(M)): # — все числа в строке различны;
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) < len(chet):
            if sum(nechet) > sum(chet):
                count += 1
print(count)