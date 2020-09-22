"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
with open("test.txt", "r") as f_obj:
    content = f_obj.readlines()
    stroka = len(content)
    print(f"Количество строк: {stroka}")
    for i in range(len(content)):
        print(f"Количество слов в строке {i+1}: {len(content[i].split())}")
