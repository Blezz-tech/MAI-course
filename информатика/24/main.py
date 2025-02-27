
def task_1():
    s = open('24.txt').readline()
    k = 0
    maxl = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 0

    print('test:', maxl)


def task_2():
    s = open('24-1.txt').readline()
    k = 0
    maxl = 0
    for i in range(len(s) - 1):
        if s[i] == 'C':
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 0

    print('1:', maxl)


task_1()
task_2()
