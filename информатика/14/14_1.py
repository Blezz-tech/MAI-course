# https://inf-ege.sdamgia.ru/test?theme=274

def task_1():
    for x in '012345678':
        for y in '012345678':
            r = int(f"88{x}4{y}", 9) + int(f"7{x}44{y}", 11)
            if r % 61 == 0:
                print('1:', r / 61)
                return None


def task_2():
    for x in "0123456789ABC":
        for y in "0123456789ABC":
            r = int(f"8{x}78{y}", 13) + int(f"79{x}{y}7", 18)
            if r % 9 == 0:
                print('2:',  r / 9)
                return None


def task_3():
    result = 99999999999
    for x in "0123456789ABCDE":
        for y in "0123456789ABCDE":
            r = int(f"90{x}4{y}", 15) + int(f"91{x}{y}2", 16)
            if r % 56 == 0:
                print('3:', r / 56)
                return None


def task_4():
    for x in "123456789A":
        for y in "0123456789A":
            r = int(f"{x}341{y}", 11) + int(f"56{x}1{y}", 19)
            if r % 305 == 0:
                print('4:', r / 305)
                return None


def task_5():
    None


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
