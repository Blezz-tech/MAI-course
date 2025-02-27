from itertools import product, permutations

print("\n## TASK TYPE 8")

# TASK 1

count = 0
for i in product('1234', repeat=5):
    if i.count('1') == 2:
        count += 1

print("- 1:", count)

# TASK 2

count = 0
for i in product('12345', repeat=5):
    if i.count('1') == 3:
        count += 1

print("- 2:", count)

# TASK 3

count = 0
for i in product('0123', repeat=3):
    if i[0] != '0' and int(i[0]) + int(i[2]) > int(i[1]):
        count += 1

print("- 3:", count)

# TASK 4

count = 0
for i in product('0123456', repeat=4):
    if i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]):
        count += 1

print("- 4:", count)

# TASK 5

count = 0
for i in product('012345678', repeat=5):
    if i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]) > int(i[4]):
        count += 1

print("- 5:", count)

# TASK 6
count = 0
for i in product("ПЯТНИЦА", repeat=5):
    if i[0] != 'Н' and i.count('Я') == 1:
        count += 1

print("- 6:", count)

# TASK 6 USING HASKELL

# main :: IO()
# main = do
#   print $ length arr
#   print $ length arr1
#   print $ length arr2
#
# arr = sequence $ replicate 5 "ПЯТНИЦА"
# arr1 = filter ((/= 'Н') . head) arr
# arr2 = filter ((== 1) . length . (filter (== 'Я')) ) arr1
#
# HASKELl END


# TASK 7

count = 0  # кол-во слов
n = 0  # номер слова
for i in permutations("МУЖЧИНА", 6):
    n += 1
    if n % 2 == 1 and \
            i[0] != 'Ч' and \
            i.count('Ж') >= 1:
        count += 1

print("- 7:", count)

# TASK 8

count = 0  # кол-во слов
n = 0  # номер слова
for i in product(sorted("АЛГОРИТМ"), repeat=5):
    n += 1
    if n % 2 == 1 and \
            i[0] != 'Г' and \
            i.count('И') >= 2:
        count += 1

print("- 8:", count)

# TASK 9

count = 0
for i in product("КОНФЕТА", repeat=5):
    if i.count('Е') == 2 and i[1] != 'Ф':
        count += 1

print("- 9:", count)

# TASK 10

count = 0
for i in product("ЕГЭ", repeat=5):
    count += 1

print('- 10:', count)

# TASK 11

count = 0
for i in product("ГОД", repeat=6):
    count += 1

print('- 11:', count)

# TASK 12

count = 0
for i in product("ЗИМА", repeat=5):
    count += 1

print('- 12:', count)

# TASK 13

count = 0
for i in product("СЛОН", repeat=5):
    if i.count('С') == 1:
        count += 1

print('- 13:', count)

# TASK 14

count = 0
for i in product("ГОД", repeat=6):
    count += 1

print('- 14:', count)

# TASK 15

count = 0
for i in product("МЕТРО", repeat=4):
    count += 1

print('- 15:', count)

# TASK 16

count = 0
for i in product("ПИР", repeat=5):
    if i.count('П') == 1:
        count += 1

print('- 16:', count)

# TASK 17

count = 0
for i in product("ABCX", repeat=5):
    if i[1] != 'X' and i[2] != 'X' and i[3] != 'X' and i[4] != 'X':
        count += 1

print('- 17:', count)

# TASK 18

count = 0
for i in product("ABCX", repeat=5):
    if i.count('X') == 1:
        count += 1

print('- 18:', count)

# TASK 19

count = 0
for i in product('УЧЕНИК', repeat=5):
    if i[0] == 'У' and i[-1] == 'К':
        count += 1

print('- 19:', count)

# TASK 27

count = 0
for i in product("МАНГУСТ", repeat=6):
    if i[0] != 'А' and i.count('У') >= 1 and i.count('М') == 2:
        count += 1

print('- 27:', count)

# TASK 29

# k = [i for i in permutations('0123456789', 4) if i[0] != '0']

chet = "02468"
nechet = "13579"

count = 0  # кол-во чисел
k = [x for x in permutations('0123456789', 4) if x[0] != '0']
ks = []

for e in k:
    n = 0
    for j in range(len(e) - 1):
        if e[j] in chet and e[j + 1] in nechet or e[j] in nechet and e[j + 1] in chet:
            n += 1
    if n == 3:
        count += 1

print('- 29:', count)

# TASK 30

count = 0
chet = "24680"
nechet = "13579"

k = [x for x in product('012345678', repeat=5) if x[0] != '0' and x.count('3') == 2]

for x in k:
    flag = True
    for j in range(len(x) - 1):
        if e[j] in nechet and e[j + 1] == '2' or e[j] == '2' and e[j + 1] in nechet:
            flag = False
    if flag:
        count += 1

print('- 30:', count)

# TASK 31

count = 0

print('- 31:', count)
