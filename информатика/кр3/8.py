count = 0

for x in "123":
    for y in "0123":
        for z in "0123":
            for w in "0123":
                for g in "0123":
                    s = x+y+z+w+g

                    v0 = s.count('3') == 1
                    v1 = s.count('03') == 0 and s.count('30') == 0

                    if v0 and v1:
                        count += 1

print(count)
