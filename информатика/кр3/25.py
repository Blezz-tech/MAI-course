from fnmatch import fnmatch
import re

count = 0


for x in range(0, 10**9 + 1, 9341):
    if fnmatch(str(x), "6?1*89*3"):
        count += 1
        print(x)

print(count)