
def task_19():
    def f(x, p):
        if x <= 49 or p > 2:
            return p == 2
        if p % 2 == 0:
            return f(x-2, p+1) and f(x-5, p+1) and f(x//3, p+1)  # проигрывает хотя бы в одном
        else:
            return f(x-2, p+1) or f(x-5, p+1) or f(x//3, p+1)  # Побеждает в любом случае

    print("19:", [s for s in range(1000, 49, -1) if f(s, 0)])
    # 1 Петя
    # 2 Ваня Побеждает


def task_20():
    def f(x, p):
        if x <= 49 or p > 3:
            return p == 3
        if p % 2 != 0:
            return f(x-2, p+1) and f(x-5, p+1) and f(x//3, p+1)  # проигрывает хотя бы в одном
        else:
            return f(x-2, p+1) or f(x-5, p+1) or f(x//3, p+1)  # Побеждает в любом случае

    print("20:", [s for s in range(1000, 49, -1) if f(s, 0)])
    # 1 Петя
    # 2 Ваня
    # 3 Петя побеждает


def task_21():
    def f(x, p):
        if x <= 49 or p > 4:
            return p == 2 or p == 4
        if p % 2 == 0:
            return f(x-2, p+1) and f(x-5, p+1) and f(x//3, p+1)  # проигрывает хотя бы в одном
        else:
            return f(x-2, p+1) or f(x-5, p+1) or f(x//3, p+1)  # Побеждает в любом случае

    print("20:", [s for s in range(1000, 49, -1) if f(s, 0)])
    # 1 Петя
    # 2 Ваня Побеждает
    # 3 Петя
    # 4 Ваня Побеждает


task_19()
task_20()
task_21()
