from itertools import product

count = 0
for i in product("ИГРА", repeat=7):
    if i.count('А') == 2:
        count += 1

print(count)