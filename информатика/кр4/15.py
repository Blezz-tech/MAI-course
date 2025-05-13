for A in range(0, 200):
    flag = True
    for (x, y) in [(x, y) for x in range(3, 300) for y in range(3, 300)]:
        v0 = (5 < y) or (x > 32) or ((x + 2*y) < A)
        if not v0:
            flag = False
            break

    if flag:
        print(A)
        break
