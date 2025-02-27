from concurrent.futures import ThreadPoolExecutor

def task_1():
    s = '8' * 68
    while ('222' in s) or ('888' in s):
        if '222' in s:
            s = s.replace('222', '8', 1)
        else:
            s = s.replace('888', '2', 1)
    return s


def task_2():
    s = "5" * 54 + "7"
    while "722" in s or "557" in s:
        if "722" in s:
            s = s.replace("722", "57", 1)
        else:
            s = s.replace("557", "72", 1)
    return s


def task_3():
    s = "9" * 65
    while "999" in s or "222" in s:
        if "222" in s:
            s = s.replace("222", "9", 1)
        else:
            s = s.replace("999", "2", 1)
    return s


def task_4():
    s = "1" + "0" * 80
    while "10" in s or "1" in s:
        if "10" in s:
            s = s.replace("10", "001", 1)
        elif "1" in s:
            s = s.replace("1", "000", 1)
    return s


def task_5():
    s = ">" +  10 * "1" + 20 * "2" + 30 * "3"
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">3" in s:
            s = s.replace(">3", "1>", 1)
    return s

def task_6():
    def process_string(n):
        s = "5" + "2" * n
        while "52" in s or "1122" in s or "2222" in s:
            if "52" in s:
                s = s.replace("52", "11", 1)
            if "2222" in s:
                s = s.replace("2222", "5", 1)
            if "1122" in s:
                s = s.replace("1122", "25", 1)
        return 1 if sum(map(int, s)) == 64 else 0

    res = 0
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_string, n) for n in range(3, 10000)]
        for future in futures:
            res += future.result()
    return res

print("1:", task_1())
print("2:", task_2())
print("3:", sum(map(int, task_3())))
print("4:", task_4().count("0"))
print("5:", sum(map(int, task_5()[:-1])))
print("6:", task_6())
