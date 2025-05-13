
def test_19():
    # -2 -5 //3
    # победитель x <= 19
    # Петя - 1, Ваня - 2
    # Победитель - Ваня первым ходом
    # Ответ - S_min
    def f(x, p):
        if x <= 19 or p > 2:
            return p == 2
        if p % 2 != 0:
            return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p + 1)
        else:
            return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p + 1)
    xs = [s for s in range(100, 19, -1) if f(s, p=0)]
    print("test_19:", min(xs))


def test_20():
    # -2 -5 //3
    # победитель x <= 19
    # Петя - 1, Ваня - 2
    # Победитель - Петя вторым ходом
    # Ответ - S_min_2
    def f(x, p):
        if x <= 19 or p > 3:
            return p == 3
        if p % 2 == 0:
            return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p + 1)
        else:
            return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p + 1)
    xs = [s for s in range(100, 19, -1) if f(s, p=0)]
    print("test_20:", xs)

def test_21():
    # -2 -5 //3
    # победитель x <= 19
    # Петя - 1, Ваня - 2
    # Победитель - Петя первым или вторым
    # Ответ - S_min
    def f(x, p):
        if x <= 19 or p > 4:
            return p == 2 or p == 4
        if p % 2 != 0:
            return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p + 1)
        else:
            return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p + 1)
    xs = [s for s in range(100, 19, -1) if f(s, p=0)]
    print("test_21:", xs)


test_19()
test_20()
test_21()

