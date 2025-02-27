user_passwd = 310 * 12

# 4096 > 2049 > 2048 -->> 2 ** 12


user_end = 14 * 8 + user_passwd

x = user_end * 128

print(user_end)
print(x, x / 1024)
print(x / 1024 / 8)