count = 0

for s in open("6.csv"):
    M = [int(x) for x in s.split(",")]

    dicts = {}

    for x in M:
        if x in dicts:
            dicts[x] += 1
        else:
            dicts[x] = 1

    unique_numbers = [x for x, count in dicts.items() if count == 1]
    repeat_numbers = [x for x, count in dicts.items() if count > 1 for _ in range(count)]

    v1 = len(unique_numbers) == 4 and len(repeat_numbers) == 2

    if not v1:
        continue

    unique_avg = sum(unique_numbers) / len(unique_numbers)
    repeat_avg = sum(repeat_numbers) / len(repeat_numbers)

    v2 = unique_avg < repeat_avg

    if not v2:
        continue

    count += 1

print(count)
