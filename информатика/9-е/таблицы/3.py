count = 0
for s in open('3,4,5.csv'):
    M = [int(x) for x in s.split(',')]

    count_dict = {}
    for x in M:
        if x in count_dict:
            count_dict[x] += 1
        else:
            count_dict[x] = 1

    unique_numbers = [x for x, count in count_dict.items() if count == 1]
    repeat_numbers = [x for x, count in count_dict.items() if count > 1 for _ in range(count)]

    v1 = len(unique_numbers) > 0 and len(repeat_numbers) > 0

    if not v1:
        continue

    unique_avg = sum(unique_numbers) / len(unique_numbers)
    repeat_avg = sum(repeat_numbers) / len(repeat_numbers)

    v2 = unique_avg > repeat_avg

    if not v2:
        continue

    count += 1

print(count)
