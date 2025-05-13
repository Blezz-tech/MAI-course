s = "1" * 2025

while "1111" in s or "5555" in s:
    if "1111" in s:
        s = s.replace("1111", "55", 1)
    else:
        s = s.replace("5555", "5", 1)

print(s)