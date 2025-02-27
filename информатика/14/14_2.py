# https://inf-ege.sdamgia.ru/test?category_id=239&filter=all

def task_1():
    for x in "012345678":
        num1 = f'4C{x}4'
        num2 = f'{x}62A'
        r = int(num1, 15) + int(num2, 13)
        if r % 121 == 0:
            print('1:', r / 121)
            return None


def task_2():
    for x in "0123456789AB":
        num1 = f'28{x}2'
        num2 = f'93{x}5'
        r = int(num1, 18) + int(num2, 12)
        if r % 133 == 0:
            print('2:', r / 133)
            break


def task_3():
    for x in "0123456789ABCDEF":
        num1 = f'2{x}84'
        num2 = f'2B3{x}'
        r = int(num1, 19) + int(num2, 16)
        if r % 88 == 0:
            print('2:', r / 88)
            return None

def task_4():
    for x in "0123456789ABCD":
        num1 = f'8{x}71'
        num2 = f'3{x}DF'
        r = int(num1, 13) + int(num2, 17)
        if r % 197 == 0:
            print('4:', r / 197)
            return None

def task_5():
    for x in "0123456789ABCD":
        num1 = f'{x}B09'
        num2 = f'{x}8E8'
        r = int(num1, 17) + int(num2, 15)
        if r % 155 == 0:
            print('5:', r / 155)
            return None

def task_6():
    None


def task_7():
    None


def task_8():
    None


def task_9():
    None


def task_10():
    None


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
task_8()
task_9()
task_10()
