from ipaddress import *

count = 0
for ip in ip_network('200.33.100.0/255.255.248.0', strict=False).hosts():
    dv = bin(int(ip))[2:]
    if dv.count('1') % 7 != 0:
        count += 1
print(count)
