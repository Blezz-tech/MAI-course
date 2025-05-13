'''f = open('9_19241.csv').readlines()
lst = [[int(x) for x in line.split(';')] for line in f]
c = 0
for x in lst:
    x.sort()
    a =[i for i in x if x.count(i) == 2]
    b =[i for i in x if x.count(i) == 1]
    if len(a) == 2 and len(b) ==3:
        if x[0] + x[-1] < x[1] + x[2] + x[3]:
            c += 1
print(c)'''

'''f = open('9_19241.csv').readlines()
lst = [[int(x) for x in line.split(';')] for line in f]
c = 0
for x in lst:
    c+=1
    a = [i for i in x if x.count(i)==3]
    b = [i for i in x if x.count(i)==1]
    if len(a) ==6 and len(b) == 1:
        if sum(a) / 6 < b[0]:
            print(c)'''

f = open('09_17550.csv').readlines()
lst = [[int(x) for x in line.split(';')] for line in f]


