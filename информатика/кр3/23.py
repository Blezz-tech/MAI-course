def f(a, b):
    if a < b or a == 16:
        return 0
    if a == b:
        return 1
    return f(a - 2, b) + (f(a // 3, b) if a % 3 == 0 else f(a // 4, b))


print(f(36, 4))
