"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл."""

import re

translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("for 5_4.txt","r", encoding='UTF-8') as count:
    for line in count:
        line = re.split(' |\n',line.rstrip())
        rus = translation[line[0]]
        line.pop(0)
        line.insert(0, rus)
        new_obj = open("new_file_5.4.txt", "a", encoding='UTF-8')
        s1 = ' '.join(line)
        new_obj.writelines(s1 + '\n')
        new_obj.close()
