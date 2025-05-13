from ipaddress import ip_network

count = 0
for ip in ip_network('249.0.33.81/255.252.0.0', 0):
    s = bin(int(ip))[2:]

    left_s = s[:16]
    right_s = s[16:]

    if right_s.count('1') / 2 > left_s.count('1'):
        count += 1

print(count)