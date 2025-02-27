import re

with open('10-16.txt', 'r', encoding='windows-1251') as file:
    text = file.read()
    count = len(re.findall(r'\bОлимп(а|у|ом|е)?\b', text))

    print("8:", count)

