import sys

sys.setrecursionlimit(2048)

def task_1():
    def f(n):
        if n == 1:
            return 1
        if n % 2 == 0:
            return n + f(n-1)
        if n > 1 and n % 2 == 1:
            return 2*f(n-2)
        return 0

    print('1:', f(26))


def task_2():
    def f(n):
        if n < 3:
            return 2 * n
        if n >= 3 and n % 2 == 0:
            return 3*n + 5 + f(n-2)
        if n >= 3 and n % 2 == 1:
            return n + 2 * f(n - 6)
        return 0

    print('2:', f(61))


def task_3():
    def f(n):
        if n < 5:
            return 1 + 2 * n
        if n >= 5 and n % 3 == 0:
            return 2 * (n + 1) * f(n-2)
        if n >= 5 and n % 3 != 0:
            return 2*n + 1 + f(n - 1) + 2*f(n - 2)
        return 0

    print('3:', f(15))


def task_4():
    def f(n):
        if n < 11:
            return n
        if n >= 11:
            return n + f(n-1)

    print('4:', f(2024)-f(2021))


def task_5():
    def f(n):
        if n > 2024:
            return n
        if n <= 2024:
            return n * f(n+1)

    print('5:', f(2022) / f(2024))


def task_6():
    def f(n):
        if n >= 2025:
            return n
        if n < 2025:
            return n + 3 + f(n + 3)

    print('6:', f(23) - f(21))


def task_7():
    def f(n):
        if n == 1:
            return 1
        if n > 1:
            return 2 * f(n-1) + g(n-1) - 2*n

    def g(n):
        if n == 1:
            return 1
        if n > 1:
            return f(n-1) + 2 * g(n - 1) + n

    print('7:', f(14) + g(14))

def task_8():
    def f(n):
        if n == 1:
            return 1
        if n > 1:
            return 3 * f(n-1) + g(n-1) - n + 5

    def g(n):
        if n == 1:
            return 1
        if n > 1:
            return f(n-1) + 3*g(n-1) - 3*n
    print('8:', f(14) + g(14))


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
task_8()
