
# xyzw - пароль
# цифра от 1 до 6

count = 0
for x in "123456":
    for y in "123456":
        for z in "123456":
            for w in "123456":
                password = x + y + z + w
                if password.count("3") == 1:
                    even_count = password.count("2") + password.count("4") + password.count("6")  # четные
                    odd_count = password.count("1") + password.count("3") + password.count("5")  # нечетные

                    if even_count <= odd_count:
                        count += 1

print(count)
