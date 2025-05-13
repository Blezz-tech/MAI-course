def task_2():
    print('y x z w r')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    r = (x <= y) and (z == (w <= x)) and not w
                    if r == 1:
                        print(y, x, z, w, int(r))


def task_5():
    def f(x):
        if x % 2 == 0:
            return str(x).replace("1", "11")
        if x % 2 == 1:
            return str(x).replace("0", "00")
    for i in range(300):
        r = f(i)
        print(i, r)
        if int(r) > 70:
            break


def task_7():
    S = 768*5120
    p = 8  # 2**8 = 256
    time = 500
    V = 655360

    r = (V * time) / (S * p)
    print("7.", r)


def task_8():
    count = 0
    lst = set()
    for x in range(100000, 999999+1):
        s = str(x)
        if s.count("0") == 1:
            i = s.find("0")

            if i == 5:
                if int(s[4]) % 2 == 0:
                    count += 1
            else:
                if int(s[i-1]) % 2 == 0 and int(s[i+1]) % 2 == 0:
                    count += 1

    print("8.", count)

    # Заменить все нечетные на 1
    # после этого проверить "101" not in s
    # "".join(list(map(lambda x: "1" if int(x) % 2 == 1 else x,"123456789")))


def task_9():
    lines = open("9var1.csv").read().split('\n')

    count = 0
    for line in lines:
        lst = line.split(',')
        a, b, c, d = lst[0], lst[1], lst[2], lst[3]
        lst = list(map(int, lst))
        lst.sort()

        v1 = a != b and a != c and a != d and b != c and b != d and c != d
        v2 = lst[-1] < sum(lst[:-1])

        if v1 and v2:
            count += 1

    print("9.", count)


def task_10():
    None




# print("## 2")
# task_2()

# print("## 3")
# task_5()

# print("## 7")
# task_7()

# print("## 8")
# task_8()

# print("## 9")
# task_9()

# print("## 10")
# task_10()


