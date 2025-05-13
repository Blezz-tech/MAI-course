from ipaddress import *

count = 0
for ip in ip_network("210.66.110.0/255.255.252.0", 0):
    ip_bin = bin(int(ip))[2:]

    if ip_bin.count('1') % 6 != 0:
        count += 1

print(count)
