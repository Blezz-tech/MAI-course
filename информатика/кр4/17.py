lst = open('17.txt').read().split('\n')
lst = list(map(int, lst))

count = 0

max_sum = 0

for i in range(len(lst) - 2):
    a, b, c = lst[i], lst[i+1], lst[i+2]
    lst1 = [a, b, c]

    neg_lst = list(filter(lambda x: x < 0, lst1))

    if max(lst1) * min(lst1) > sum(neg_lst):
        count += 1

        max_sum = max(max_sum, sum(lst1))

print(count, max_sum)
