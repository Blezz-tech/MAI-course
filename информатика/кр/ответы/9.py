count = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(",")]
    if len(M) == len(set(M)): # — все числа в строке различны;
        M.sort()
        if ((M[0]+M[1]+M[2]+M[3]) == M[4]):
            count += 1
print(count)