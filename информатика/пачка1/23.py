# Не моё
def f(x,p):
    if x<=21 or p>4:
        return p==2 or p==4
    if p%2 != 0:
        return f(x-3, p+1) or f(x-7, p+1) or f(x//4, p+1)
    else:
        return f(x - 3, p + 1) and f(x - 7, p + 1) and f(x // 4, p + 1)

print ([s for s in range(1000, 21, -1) if f(s,0)])