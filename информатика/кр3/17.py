lst = open('17.txt').read().split('\n')
lst = list(map(int, lst))

max_chet = max(list(filter(lambda x: x % 2 == 0, lst)))

count = 0
max_sum = 0

for i in range(len(lst) - 1):
    a, b = lst[i], lst[i+1]

    if (a + b) == max_chet:
        count += 1
        max_sum = max(max_sum, a**2 + b**2)

print(count, max_sum)