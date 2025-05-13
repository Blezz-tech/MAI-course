S = 3840 * 2160
k = 17
V = S * k

S1 = 1280*720
k1 = 5
V1 = S1 * k1

dV = V - V1
print('dV = V - V1 =', V, '-', V1, '=', dV)

print(dV*120/8/1024)



