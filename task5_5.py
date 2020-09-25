"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

import random
import re

with open("text2.txt", "w", encoding='UTF-8') as f_obj:
    f_obj.writelines(str(random.randint(1, 100)) + ' ' for _ in range(10))  # вводим 10 цифр до 100
with open("text2.txt", "r", encoding='UTF-8') as sum_chisel:
    lis_avg = [re.split(' |\n', line.rstrip())for line in sum_chisel]
    sum_chis = [int(num) for num in lis_avg[0]]
    print("Были введены такие цифры: ", *lis_avg)
    print(f"Cумма чисел в файле {sum(sum_chis)}")
