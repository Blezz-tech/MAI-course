def f(k):
    s = ""
    while k:
        s = str(k % 5) + s
        k //= 5
    return s


for x in range(2735, 0, -1):
    if f(5**2025 + 5**1500 - x).count('0') == 527:
        print(x)
        break
