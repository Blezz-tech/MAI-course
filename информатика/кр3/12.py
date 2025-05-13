S = "1" * 2026

while "11111" in S or "222" in S:
    if "11111" in S:
        S = S.replace("11111", "22", 1)
    else:
        S = S.replace("222", "2", 1)

print(S)
