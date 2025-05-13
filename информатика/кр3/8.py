
def convert(x):
    n = ""
    while x:
        n += str(x % 7)
        x //= 7
    return n[::-1]


count = 0



count = 0

for a in "123456":
    for b in "0123456":
        for c in "0123456":
            for d in "0123456":
                for e in "0123456":
                    for f in "0123456":
                        s = a+b+c+d+e+f
                        s1 = s.replace("2", "$")\
                            .replace("4", "$")\
                            .replace("6", "$")
                        if s.count("0") == 1\
                            and "$0" not in s1\
                            and "0$" not in s1:
                            count += 1
                            # print(s1)

# for x in range(16807, 117649):
#     x = str(convert(x))
#     if x.count("0") == 1:
#         pos = x.find("0")
#         if pos == 5:
#             if int(x[5]) % 2 == 1:
#                 count += 1
#         elif (int(x[pos - 1]) % 2 == 1) and (int(x[pos + 1]) % 2 == 1):
#             count += 1

print(count)
