from itertools import permutations, product

def task_1():
    with open('17-1.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []
        for i in range(len(lst) - 1):
            a, b = lst[i], lst[i+1]
            if a % 3 == 0 or b % 3 == 0:
                sum_lst.append(a+b)

        print('1:', len(sum_lst), max(sum_lst))

def task_2():
    with open('17-2.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []
        for i in range(len(lst) - 1):
            for j in range(i+1, len(lst)):
                a, b = lst[i], lst[j]
                v1 = a % 160 != b % 160
                v2 = a % 7 == 0 or b % 7 == 0
                if v1 and v2:
                    sum_lst.append(a+b)

        print('2:', len(sum_lst), max(sum_lst))


def task_3():
    with open('17-3.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                a, b = lst[i], lst[j]
                v1 = (a - b) % 2 == 0
                v2 = a % 31 == 0 or b % 31 == 0
                if v1 and v2:
                    sum_lst.append(a+b)

        print('3:', len(sum_lst), max(sum_lst))


def task_4():
    with open('17-4.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                a, b = lst[i], lst[j]
                v1 = (a * b) % 10 == 0
                if v1:
                    sum_lst.append(a+b)

        print('4:', len(sum_lst), max(sum_lst))


def task_5():
    with open('17-5.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []

        even_lst = list(filter(lambda x: x % 2 == 0, lst))
        avg_of_lst = sum(even_lst) / len(even_lst)
        for i in range(len(lst) - 1):
            a, b = lst[i], lst[i+1]
            v1 = a % 3 == 0 or b % 3 == 0
            v2 = a < avg_of_lst or b < avg_of_lst
            if v1 and v2:
                sum_lst.append(a+b)

        print('5:', len(sum_lst), max(sum_lst))


def task_6():
    with open('17-6.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []

        min_of_lst = min(filter(lambda x: x % 21 == 0, lst))
        for i in range(len(lst) - 1):
            a, b = lst[i], lst[i+1]
            v1 = a % min_of_lst == 0 or b % min_of_lst == 0
            if v1:
                sum_lst.append(a+b)

        print('6:', len(sum_lst), max(sum_lst))


def task_7():
    with open('17-7.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []

        max_of_lst = max(filter(lambda x: str(x)[-1] == '3', lst))
        for i in range(len(lst) - 1):
            a, b = lst[i], lst[i+1]
            v1 = (str(a)[-1] == '3') != (str(b)[-1] == '3')
            v2 = (a**2 + b**2) >= max_of_lst**2
            if v1 and v2:
                sum_lst.append(a**2 + b**2)

        print('7:', len(sum_lst), max(sum_lst))


def task_8():
    with open('17-8.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []

        max_of_lst = max(filter(lambda x: str(x)[-2:] == '13', lst))
        for i in range(len(lst) - 2):
            a, b, c = lst[i], lst[i+1], lst[i+2]
            v1 = len(list(filter(lambda x: len(str(x)) == 3, [a, b, c]))) == 2
            v2 = (a + b + c) <= max_of_lst
            if v1 and v2:
                sum_lst.append(a+b+c)

        print('8:', len(sum_lst), max(sum_lst))


def task_9():
    def is_5_digit(n):
        n = str(n)
        if n[0] == "-":
            return len(n[1:]) == 5
        return len(n) == 5

    with open('17-9.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []

        max_of_lst = max(filter(lambda x: str(x)[-2:] == '29', lst))
        for i in range(len(lst) - 2):
            a, b, c = lst[i], lst[i+1], lst[i+2]
            v1 = 2 == len(list(filter(is_5_digit, [a, b, c])))
            v2 = (a + b + c) <= max_of_lst
            if v1 and v2:
                sum_lst.append(a+b+c)

        print('9:', len(sum_lst), max(sum_lst))


def task_10():
    def f_is_simple(n):
        is_simple = True
        for elem in range(2, n):
            if n % elem != 0:
                is_simple = False
                break
        return is_simple

    with open('17-10.txt', 'r') as file:
        lst = file.read().split('\n')
        lst = [line for line in lst if line]
        lst = list(map(int, lst))
        sum_lst = []

        for i in range(len(lst) - 2):
            a, b, c = lst[i], lst[i+1], lst[i+2]
            v1 = "3" in str(a) and '3' in str(b) and '3' in str(c)
            v2 = f_is_simple(a + b + c)
            if v1 and v2:
                sum_lst.append(a+b+c)

        print('10:', len(sum_lst), max(sum_lst))


# task_1()
# task_2()
# task_3()
# task_4()
# task_5()
# task_6()
# task_7()
# task_8()
# task_9()
# task_10()

# 1+
# 2+
# 3+
# 4+
# 5+
# 6+
# 7+
# 8+
# 9+
# 10+
