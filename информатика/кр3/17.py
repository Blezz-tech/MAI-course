f = open('17.txt').readlines()
lst = [int(line) for line in f]

min_item = min(lst)

lst_count = 0
lst_sum = lst[0] + lst[1]
for i in range(len(lst) - 1):
    a, b = lst[i], lst[i+1]

    v1 = a % 30 == min_item or b % 30 == min_item
    if v1:
        lst_count += 1
        lst_sum = min(lst_sum, a+b)

print(lst_count, lst_sum)
