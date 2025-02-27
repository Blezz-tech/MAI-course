import re

with open('10-0.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\b[Пп]ортрет\b', text))
    print("1:", count)

with open('10-0.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\b[Дд]ень\b', text))
    print("2:", count)

with open('10-0.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\bсупруг\b', text))
    print("3:", count)

with open('10-0.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\b[Дд]верь\b', text))
    print("4:", count)

with open('10-1.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\b[Оо]н\b', text))
    print("5:", count)

with open('10-1.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\b(я|ты|он|она|оно)\b', text, flags=re.IGNORECASE))
    print("6:", count)

with open('10-15.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\b[Вв]\b', text))
    print("7:", count)

with open('10-16.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\bОлимп(а|у|ом|е)?\b', text))
    print("8:", count)

with open('10-17.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'Милон\. ', text))
    print("9:", count)

with open('10-18.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    count = len(re.findall(r'не ', text))
    print("10:", count)


