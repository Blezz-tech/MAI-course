
def f(k):
    s = ""
    while k:
        s = str(k % 9) + s
        k //= 9
    return s


for x in range(5769, 0, -1):
    if f(9**2025 + 9**1000 - x).count('0') == 1026:
        print(x)
        break
