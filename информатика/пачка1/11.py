from math import floor
# 10 + 500 = 510 => достаточно 512 => 9 бит на символ
k = 9

s = 244 * 1024
count = 1600

per_count = s / count

print(per_count, "~=", floor(per_count))
c = 156

len_id = 156 * 8 / 9
print(len_id, "~=", floor(len_id))
