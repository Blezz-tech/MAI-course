import sys

sys.setrecursionlimit(30000)


def f(x):
    if x == 1:
        return 1
    return x + f(x - 1)


print(f(3000) - f(2000))
