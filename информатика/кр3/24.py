# QRW 124

s = open("24.txt").readline()

max_len = 0
curr_len = 0

for i in range(len(s) - 1):
    if (s[i] in "QWR") != (s[i+1] in "124"):
        curr_len += 1
    else:
        max_len = max(max_len, curr_len)
        curr_len = 0

print(max_len)