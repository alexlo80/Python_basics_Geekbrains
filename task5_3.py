"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
import statistics
import re

with open("oklad.txt", encoding='UTF-8') as oklad:
    print("Фамиилии тех, кто получает меньше 20000: ", end="")
    print(*[re.split(' |\n', line.rstrip())[0] for line in oklad if int(re.split(' |\n', line.rstrip())[1]) < 20000])
with open("oklad.txt", encoding='UTF-8') as oklad:
    lis_avg = [int(re.split(' |\n', line.rstrip())[1]) for line in oklad]
    avg = statistics.mean(lis_avg)
print(f"Средний оклад сотрудников: {avg}")
