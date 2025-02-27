from itertools import product

print("\n## TASK TYPE 8")

print("\n### TASK 1")

count = 0
for i in product('1234', repeat=5):
    if i.count('1') == 2:
        count += 1

print("\nanswer:", count)

print("\n### TASK 2")

count = 0
for i in product('12345', repeat=5):
    if i.count('1') == 3:
        count += 1

print("\nanswer:", count)

print("\n### TASK 3")

count = 0
for i in product('0123', repeat=3):
    if i[0] != '0' and int(i[0]) + int(i[2]) > int(i[1]):
        count += 1

print("\nanswer:", count)

print("\n### TASK 4")

count = 0
for i in product('0123456', repeat=4):
    if i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]):
        count += 1

print("\nanswer:", count)

print("\n### TASK 5")

count = 0
for i in product('012345678', repeat=5):
    if i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]) > int(i[4]):
        count += 1

print("\nanswer:", count)
