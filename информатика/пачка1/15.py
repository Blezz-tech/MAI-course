B = list(range(200, 301))

def f(x, A):
    return (x % A == 0) or ((x in B) <= (not (x % 77 == 0)))

for A in range(1000, 1, -1):
    results = []
    for x in range(1, 2**20):
        results.append(f(A, x))

    print(results)
    if all(results):
        print(A)
        break

