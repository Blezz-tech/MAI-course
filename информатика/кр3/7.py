from math import floor

S = 1024*100

V = 75 * 1024 * 8

x = V * 1.35

k = x / S

print(k)

k = floor(k)
print(k, 2**k)

