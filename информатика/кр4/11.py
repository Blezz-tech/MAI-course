from math import floor

x = 257

V = 33 * 1024 * 1024

count = 295740

per_count = V / count
per_count = floor(per_count)

print(per_count)
print(per_count / 257)
