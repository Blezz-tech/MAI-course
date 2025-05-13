from ipaddress import ip_network

count = 0

for ip in ip_network('143.168.72.213/255.255.255.240', 0):
    print(ip)
    None

print(count)
