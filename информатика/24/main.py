
def task_0():
    s = open('./v2/24.txt').read()
    k = 0
    maxl = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 1

    print('0:', maxl)


def task_1():
    s = open('24-1.txt').read()
    k = 0
    maxl = 0
    for i in range(len(s)):
        if s[i] == 'C':
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 1

    print('1:', maxl)


def task_2():
    s = open("24-2.txt").read()
    k = 0
    maxl = 0
    for i in range(len(s)):
        if s[i] in "ABC":
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 0

    print("2:", maxl)


def task_3():
    s = open("24-3.txt").read()
    k = 0
    maxl = 0
    for i in range(len(s)):
        if s[i] != 'D':
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 0

    print("3:", maxl)


def task_4():
    s = open("24-4.txt").read()
    k = 0
    maxl = 0

    for i in range(len(s)):
        if s[i] not in 'AE':
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 0

    print("4:", maxl)


def task_7():
    s = open("24-7.txt").read()
    k = 0
    maxl = 0

    for i in range(len(s) - 1):
        if s[i:i+2] != 'ad' and s[i:i+2] != 'da':
            k += 1
            if k > maxl:
                maxl = k
        else:
            k = 0

    print("7:", maxl)


def task_8():
    s = open("24-8.txt").read()
    k = 0
    maxl = 0

    i = 0
    while i < len(s) - 1:
        v_1 = s[i] in "CDF"
        v_2 = s[i+1] in "AO"
        if v_1 and v_2:
            k += 1
            i += 1
            if k > maxl:
                maxl = k
        else:
            k = 0
        i += 1

    print("8:", maxl)


def task_9():
    lines = open("./v2/24-9.txt").readlines()

    k = 0
    for s in lines:
        if s.count("YZ") > 1:
            k += 1

    print("9:", k)


# def task_10():
#     import re
#     lines = open("24-9.txt").readlines()
#
#     count = 0
#     for s in lines:
#         if re.search(r"Y.Z", s):
#             count += 1
#
#     print("10:", count)


def task_10():
    import re
    lines = open("24-9.txt").readlines()

    count = 0
    for line in lines:
        for i in range(len(line) - 2):
            if line[i] == 'F' and line[i+2] == 'O':
                count += 1
                break

    print("10:", count)


# def task_13():
#     s = open("24-13.txt").read()
#     maxl = 0
#
#     for i in range(len(s) - 1):
#         for j in range(i + 1, len(s)):
#             q = s[i:j]
#             q_len = j - i
#             if q_len > maxl:
#                 if q.count('DE') <= 240:
#                     maxl = q_len
#
#     print("13:", maxl)


def task_13():
    f = open("24-13.txt").read()
    s = f.replace('DE', 'D E')
    s = s.split()
    maxi = 0
    for i in range(len(s)):
        r = ''.join(s[i:i + 241])
        maxi = max(maxi, len(r))
    print("13:", maxi)


def task_14():
    # Не работает
    s = open("2025_24.txt").read()
    

    for i in s:
        if

    s = s.split()
    print(s)
    maxl = 0
    for i in s:
        maxl = max(maxl, len(i))

    print("14:", maxl)


task_0()
task_1()
task_2()
task_3()
task_4()
task_7()
task_8()
task_9()
task_10()
task_13()
task_14()
