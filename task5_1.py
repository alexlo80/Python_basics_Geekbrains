""" 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open("text.txt", "a", encoding='UTF-8') as f_obj:
    line = input('Введите текст ')
    while line:
        f_obj.writelines(line + '\n')
        line = input('Введите текст ')
        if not line:
            break
