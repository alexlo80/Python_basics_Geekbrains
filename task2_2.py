"""2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input()."""
my_list = []
while True:
    user_input = input('Please fill in my list with elements, or type "break" to stop')
    if user_input == "break":
        break
    my_list.append(user_input)
print(my_list)
size = len(my_list)
number_of_par = size // 2
for par in range(number_of_par):
    my_list[par * 2], my_list[par * 2 + 1] = my_list[par * 2 + 1], my_list[par * 2]
    print(my_list)