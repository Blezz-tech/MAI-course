def f3(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f3(x + 3, y) + f3(x + 4, y) + f3(x + 5, y)


def f4(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f4(x + 1, y) + f4(x + 2, y) + f4(x * 2, y)


def f7(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f7(x + 1, y) + f7(x + 2, y) + f7(x * 3, y)

# Долго вычисляется, нужна оптимизация
# def f7_1(x, y):
#     if x > y or x == 40:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f7_1(x + 1, y) + f7_1(x + 8, y) + f7_1(x * x, y)


# def f7_1(x, y):
#     def helper(x, y, acc):
#         if x > y or x == 40:
#             return acc
#         if x == y:
#             return acc + 1
#         else:
#             return helper(x + 1, y, acc) + helper(x + 8, y, acc) + helper(x * x, y, acc)
#
#     return helper(x, y, 0)

def f8(x, y):
    if x > y or x == 6 or x == 12:
        return 0
    if x == y:
        return 1
    if x < y:
        return f8(x + 1, y) + f8(x * 2, y) + f8(x + 3, y)


def f9(x, y):
    if x > y or x == 5 or x == 10:
        return 0
    if x == y:
        return 1
    if x < y:
        return f9(x + 1, y) + f9(x * 2, y) + f9(x + 3, y)


def f10(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    if x < y:
        return f10(x + 1, y) + f10(x + 2, y)


def f11(x, y):
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    if x < y:
        return f11(x + 1, y) + f11(x + 2, y)


def f12(x, y):
    if x > y or x == 17:
        return 0
    if x == y:
        return 1
    if x < y:
        return f12(x + 1, y) + f12(x * 2, y)


def f13(x, y):
    if x > y or x == 17:
        return 0
    if x == y:
        return 1
    if x < y:
        return f13(x + 1, y) + f13(x * 2, y)

def f14(x, y, k):
    if x > y + 1:
        return 0
    if x == y:
        return 1
    else:
        if k == 1:
            return f14(x * 2, y, k - 1) + f14(x * 3, y, k - 1)
        else:
            return f14(x - 1, y, k + 1) + f14(x * 2, y, k) + f14(x * 3, y, k)


def f14_v1(x, y):
    if x > y + 1:
        return 0
    if x == y:
        return 1
    else:
        return f14_v1_a(x - 1, y) + f14_v1(x * 2, y) + f14_v1(x * 3, y)


def f14_v1_a(x, y):
    if x > y + 1:
        return 0
    if x == y:
        return 1
    else:
        return f14_v1(x * 2, y) + f14_v1(x * 3, y)


def f15(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f15(x + 1, y) + f15(x + 2, y) + f15_c(x * 2, y)


def f15_c(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f15(x + 1, y) + f15(x + 2, y)


def f16(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f16(x - 2, y) + f16(x // 2, y)


def f17(s, p, A, C):
    if not p:
        return s
    c, p = p[0], p[1:]

    if c == '1':
        return f17(s + 3, p, A, C)
    if c == '2':
        return f17(s * A, p, A, C)
    if c == '3':
        return f17(s + C, p, A, C)


def f17_v1(x, A, C):
    def go_1(x):
        return x + 3
    def go_2(x):
        return x * A
    def go_3(x):
        return x + C

    return go_3(go_2(go_1(go_3(go_2(go_3(go_1(x)))))))


answers = [
    ["3", f3(22, 42)],
    ["4", f4(3, 10) * f4(10, 12)],
    ["7", f7(1, 8) * f7(8, 15)],
    # ["7.1", f7_1(2, 100)],
    ["8", f8(3, 16)],
    ["9", f9(2, 14)],
    ["10", f10(3, 9) * f10(9, 20)],
    ["11", f11(2, 9) * f11(9, 18)],
    ["12", f12(1, 10) * f12(10, 21)],
    ["13", f13(1, 10) * f13(10, 35)],
    ["14", f14(3, 20, 0)],
    ["14_v1", f14_v1(3, 20)],
    ["15", f15(1, 11)],
    ["16", f16(38, 16) * f16(16, 2)]
]

for index, x in answers:
    print(f"f{index}: {x}")


for A in range(1, 100 + 1):
    for C in range(1, 100 + 1):
        if f17_v1(5, A, C) == 329:
            print(f"f17_v1: A: {A}")
            print(f"f17_v1: C: {C}")
            print(f"f17_v1: A + C: {A + C}")
            break

for A in range(1, 100 + 1):
    for C in range(1, 100 + 1):
        if f17(5, "1323123", A, C) == 329:
            print(f"f17: A: {A}")
            print(f"f17: C: {C}")
            print(f"f17: A + C: {A + C}")
            break