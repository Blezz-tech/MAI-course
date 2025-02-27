def f1(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f1(x+3, y) + f1(x+4, y) + f1(x+5, y)

def f7_1(x, y):
    if x > y or x == 40:
        return 0
    if x == y:
        return 1
    else:
        return f7_1(x + 1, y) + f7_1(x + 8, y) + f7_1(x * x, y)

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

def f10(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    else:
        return f1(x + 1, y) + f1(x + 2, y)

answers = [
    # ["1", f1(22, 42)],
    # ["7.1", f7_1(2, 100)],
    ["10", f10(3, 9)*f10(9,20)],
]

for index, x in answers:
    print(f"f{index}: {x}")
