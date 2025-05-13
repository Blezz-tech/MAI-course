def nods(x,
         count,
         include_1=False,
         include_x=False,
         v=lambda x: True
         ):
    lst = []
    if include_1:
        lst.append(1)

    for i in range(2, x):
        if x % i == 0 and v(i):
            lst.append(i)
        if len(lst) > count:
            return []

    if include_x:
        lst.append(x)
    if len(lst) != count:
        return []
    return lst


def task_1():
    print("\ntask_1")
    x_lst = []
    for i in range(174457, 174505 + 1):
        nods_lst = nods(i, 2)

        if nods_lst:
            x_lst.append((nods_lst[0], nods_lst[1]))
    x_lst = sorted(x_lst, key=(lambda x: x[0] * x[1]))
    x_lst = list(map(lambda x: f"{x[0]} {x[1]}", x_lst))
    print('\n'.join(x_lst))


def task_2():
    print("\ntask_2")

    for i in range(164700, 164752 + 1):
        nods_lst = nods(i, 6, include_1=True, include_x=True)

        if nods_lst:
            print(' '.join(map(str, nods_lst)))


def task_3():
    print("\ntask_3")

    for i in range(190201, 190230 + 1):
        nods_lst = nods(i, 4, include_1=True, include_x=True)

        if nods_lst:
            print(' '.join(map(str, nods_lst[::-1])))


def task_4():
    print("\ntask_4")

    for i in range(190061, 190080 + 1):
        nods_lst = nods(
            i,
            4,
            include_1=True,
            include_x=True,
            v=lambda x: x % 2 == 1
        )

        if nods_lst:
            print(' '.join(map(str, nods_lst[::-1])))


def task_5():
    print("\ntask_5")

    def nodes(x):
        nod_min = 0
        nod_max = 0

        for i in range(2, x):
            if x % i == 0:
                nod_min = i
                break

        for i in range(x+1, 1):
            if x % i == 0:
                nod_max = i
                break

        if nod_min == 0 or nod_max == 0 or nod_max == nod_min:
            return 0

        return nod_min + nod_max



    for i in range(700000, 800000):
        nod_sum = nodes(i)

        if nod_sum != 0:
            print(i, nod_sum)

def task_6():
    None


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
