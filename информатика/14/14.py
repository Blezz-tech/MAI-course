# 3. Операнды арифметического выражения записаны в системе
# счисления с основанием 47:
# 1x24A47 + x202447 – 6x0847
# В записи чисел переменная x обозначает некоторую ненулевую цифру
# из алфавита 47-ричной системы счисления. Определите наименьшее
# значение x, при котором значение данного арифметического выражения
# кратно 46. Для найденного x вычислите значение данного арифметического
# выражения и укажите его в ответе в десятичной системе счисления.

def task_1_1():
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

    for x in range(47):
        x1 = convert('1*24A', x, 47)
        x2 = convert('*2024', x, 47)
        x3 = convert('6*08', x, 47)
        result = x1 + x2 - x3
        if result % 46 == 0:
            print('1_1:', result)
            return None


def task_1_2():
    for i in range(47):
        # 1x24A + x2024 – 6x08
        x = 1*47**4 + i*47**3 + 2*47**2 + 4*47 + 10
        y = i*47**4 + 2*47**3 + 0*47**2 + 2*47 + 4
        z = 6*47**3 + i*47**2 + 0*47 + 8

        r = x + y - z
        if r % 46 == 0:
            print('1_2:', r)
            return None

# Операнды арифметического выражения записаны в системе
# счисления с различными основаниями:
# 34x558 + 12x761 + x45667 – x5y772
# В записи чисел x и y (x > 0) обозначают неизвестные цифры из алфавита
# соответствующей системы счисления. Определите значения x и y, при которых
# значение данного арифметического выражения положительно и кратно 363.
# В ответе запишите сумму найденных значений x и y.

def task_2_1():
    def convert(num, x, y, base):
        res = 0
        for i, v in enumerate(num, start=1):
            if v == '*':
                res += x * base ** (len(num) - i)
            elif v == '%':
                res += y * base ** (len(num) - i)
            elif v.isalpha():
                res += (ord(v) - 55) * base ** (len(num) - i)
            else:
                res += int(v) * base ** (len(num) - i)
        return res

    sum = 0
    for x in range(1, 58):
        for y in range(72):
            # 34x5_58 + 12x7_61 + x456_67 – x5y7_72
            x1 = convert('34*5', x, y, 58)
            x2 = convert('12*7', x, y, 61)
            x3 = convert('*456', x, y, 67)
            x4 = convert('*5%7', x, y, 72)
            r = x1 + x2 + x3 - x4
            if r % 363 == 0 and r > 0:
                sum += x + y
    print('2_1:', sum)


def task_2_2():
    sum = 0
    for x in range(1, 58):
        for y in range(72):
            # 34x5_58 + 12x7_61 + x456_67 – x5y7_72
            x1 = 3*58**3 + 4*58**2 + x*58 + 5
            x2 = 1*61**3 + 2*61**2 + x*61 + 7
            x3 = x*67**3 + 4*67**2 + 5*67 + 6
            x4 = x*72**3 + 5*72**2 + y*72 + 7
            r = x1 + x2 + x3 - x4
            if r % 363 == 0 and r > 0:
                sum += x + y
    print('2_2:', sum)


task_1_1()
task_1_2()
task_2_1()
task_2_2()
