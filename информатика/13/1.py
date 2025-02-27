from ipaddress import *


def v1():
    count = 0
    for ip in ip_network('106.184.0.0/255.248.0.0').hosts():
        dv = bin(int(ip))[2:]
        if dv.count('1') % 2 != 0:
            count += 1
    print('1:', count)


def v2():
    count = 0
    for ip in ip_network('112.160.0.0/255.240.0.0').hosts():
        dv = bin(int(ip))[2:]
        if dv.count('1') % 5 == 0:
            count += 1
    print('2:', count)


def v3():
    for i in range(32):
        mask = ip_network(f"15.51.208.15/{i}", 0)
        # print(mask)
        if str(mask).split('/')[0] == '15.51.192.0':
            print('3:', i)
            break

def v4():
    minn = 2 ** 32
    for i in range(32):
        net1 = ip_network(f"195.157.132.140/{i}", 0)
        net2 = ip_network(f"195.157.132.176/{i}", 0)

        sp1 = str(net1).split('/')[0]
        sp2 = str(net2).split('/')[0]
        if (sp1 == sp2):
            k = net1.num_addresses
            if k < minn:
                minn = k
    print('4:', minn)

def v5():
    for i in range(32, 0, -1):
        net1 = ip_network(f"118.222.130.140/{i}", 0)
        net2 = ip_network(f"118.222.201.140/{i}", 0)

        sp1 = str(net1).split('/')[0]
        sp2 = str(net2).split('/')[0]
        if (sp1 == sp2):
            print('5:', str(net1.netmask)[:3])
            break


def v6():
    k = 0
    for ip in ip_network('102.141.0.0/255.255.192.0'):
        dv = bin(int(ip))[2:]
        # print(dv)
        if dv.count('1') % 7 == 0 and dv.endswith('1011'):
            k += 1
    print('6:', k)


def v7():
    None


def v8():
    None


def v9():
    None


v1()
v2()
v3()
v4()
v5()
v6()
v7()
v8()
v9()
