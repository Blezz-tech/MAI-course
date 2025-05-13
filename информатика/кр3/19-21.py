
def task_19():
    def f(x, h):
        if h == 3 and x <= 49:
            return 1
        elif h == 3 and x > 49:
            return 0
        elif x <= 49 and h < 3:
            return 0
        else:
            if h % 2 == 0:
                return f(x - 2, h + 1) or f(x - 5, h + 1) or f(x // 3, h + 1)  # стратегия победителя
            else:
                return f(x - 2, h + 1) or f(x - 5, h + 1) or f(x // 3, h + 1)  # стратегия проигравшего(неудачный ход)

    for x in range(50, 200):
        if f(x, 1) == 1:
            print("19:", x)
            break


def task_20():
    None


def task_21():
    None


task_19()
task_20()
task_21()
