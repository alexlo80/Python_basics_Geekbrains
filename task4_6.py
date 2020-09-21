"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""


from itertools import count
from itertools import cycle

# первое задание
start = int(input("c  какого числа: "))
finish = int(input("до  какого числа: "))
for i in count(start):
    if i > finish:
        break
    else:
        print(i)


# второе задание
spis = ['first', 'second', 'third', 'fourth']
iterator = cycle(spis)
 
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator)) 
print()

# еще одна опция второго задания
count = 0
for item in cycle(spis):
    if count > 10:
        break
    print(item)
    count += 1
