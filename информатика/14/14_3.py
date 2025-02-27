# https://inf-ege.sdamgia.ru/test?filter=all&category_id=220&sort=

def task_72599():
    def convert(num, x, base):
        res = 0
        for i, v in enumerate(num, start=1):
            if v == '*':
                res += x * base ** (len(num) - i)
            elif v.isalpha():
                res += (ord(v) - 55) * base ** (len(num) - i)
            else:
                res += int(v) * base ** (len(num) - i)
        return res

    for x in range(38, 0, -1):
        num1 = convert('C59*BA98F', x, 37)
        num2 = convert('E3*5DA9C6', x, 37)
        if (num1 * num2) % 36 == 0:
            print('72599:', convert(f'2*1', x, 37))
            return None


# Тип 14 № 47218
def task_47218():
    for x in '0123456789ABCDE':
        num1 = f'123{x}5'
        num2 = f'1{x}233'
        r = int(num1, 15) + int(num2, 15)
        if r % 14 == 0:
            print('47218:', r / 14)
            return None


# Тип 14 № 68276
def task_68276():
    def convert(num, x, base):
        res = 0
        for i, v in enumerate(num, start=1):
            if v == "*":
                res += x
            elif v.isalpha():
                res += (ord(v) - 55) * base ** (len(num) - i)
            else:
                res += int(v) * base ** (len(num) - 1)
        return res

    for p in range(15, 300):
        x1 = convert("AB967D8", 0, p)
        x2 = convert("E435A98", 0, p)
        if (x1 + x2) % (p - 1) == 0:
            print('68276:', p)
            return None


task_72599()
task_47218()
task_68276()
