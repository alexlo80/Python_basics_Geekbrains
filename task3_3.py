"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    sort = sorted(arg_list)
    summ = sort[-1] + sort[-2]
    return summ


while True:    
    arg1 = input("Введи первое число: ")
    arg2 = input("Введи второе число: ")
    arg3 = input("Введи третье число: ")
    if arg1.isdigit() and arg2.isdigit() and arg3.isdigit():
        arg1, arg2, arg3 = int(arg1), int(arg2), int(arg3)
        break
    else:
        print("Введи только числа, Товарищ пользователь")
        
print(f"Результат суммы самых больших цифр : {my_func(arg1,arg2,arg3)}")
