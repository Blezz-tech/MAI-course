from math import ceil

s_len = 310

# 1000 + 10 = 1010 Подойдёт 1024 -- 10 бит на символ

V_na_s = ceil(s_len * 10 / 8)


print(V_na_s*8960 / 1024)
