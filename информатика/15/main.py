
def task_1():
    def dell(n, m):
        return n % m == 0

    lst = []
    for A in range(1, 2**10):
        is_dell = True
        for x in range(1, 2**10):
            v1 = not dell(x, A)
            v2 = dell(x, 6)
            v3 = not dell(x, 9)
            r = v1 <= (v2 <= v3)
            if not r:
                is_dell = False
                break

        if is_dell:
            lst.append(A)

    print('1:', max(lst))

def task_2():
    def dell(n, m):
        return n % m == 0

    for A in range(1, 2**10):
        is_dell = True
        for x in range(1, 2**15):
            v1 = dell(A, 40)
            v2 = dell(780, x)
            v3 = not dell(A, x)
            v4 = not dell(180, x)
            r = v1 and (v2 <= (v3 <= v4))
            if not r:
                is_dell = False
                break
        if is_dell:
            print('2:', A)
            return None


def task_3():
    def dell(n, m):
        return n % m == 0

    for A in range(1, 2**10):
        is_dell = True
        for x in range(1, 2**10):
            v1 = dell(x, 15)
            v2 = not dell(x, 21)
            v3 = not dell(x, A)
            v4 = not dell(x, 15)
            # r = (v1 and v2) <= (v3 or v4)
            r = (x % 15 == 0 and x % 21 != 0) <= (x % A != 0 and x % 15 != 0)
            if not r:
                is_dell = False
                break
        if is_dell:
            print('3:', A)
            return None


def task_4():
    for A in range(2*10, -1, -1):
        is_dell = True
        for x in range(2**10):
            for y in range(2**10):
                v1 = 48 != y + 2*x
                v2 = A < x
                v3 = A < y
                r = v1 or v2 or v3
                if not r:
                    is_dell = False
                    break
        if is_dell:
            print('4:', A)
            return None

def task_5():
    for A in range(2**10):
        is_dell = True
        for x in range(2**8):
            for y in range(2**8):
                v1 = x + 2*y < A
                v2 = y > x
                v3 = x > 60
                r = v1 or v2 or v3
                if not r:
                    is_dell = False
                    break
        if is_dell:
            print('5:', A)
            return None

def task_6():
    for A in range(2**8, 0, -1):
        for x in range(2**8):
            for y in range(2**8):
                v1 = x + 2 * y > 48
                v2 = y > x
                v3 = x + 3 * y < A
                r = v1 or v2 or v3
                if not r:
                    print('6:', A)
                    return None

def task_7():
    for A in range(2**8, -1, -1):
        is_dell = True
        for x in range(2**8):
            for y in range(2**8):
                v1 = x + 2 * y > A
                v2 = x > 13
                v3 = y < 44
                r = v1 or v2 or v3
                if not r:
                    is_dell = False
                    break
        if is_dell:
            print('7:', A)
            return None

# Не работает
def task_8():
    for A in range(2**15, 0, -1):
        is_dell = True
        for x in range(-2 ** 7, 2 ** 7):
            for y in range(-2 ** 7, 2 ** 7):
                v = (x + 2 * y > A) or (x > 13) or (y < 44)
                if not v:
                    is_dell = False
                    break

        if is_dell:
            print('8:', A)
            return None


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
task_8()
