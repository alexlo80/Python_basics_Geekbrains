"""4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""


def is_valid_decimal(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def is_valid_int(z):
    try:
        int(z)
    except ValueError:
        return False
    else:
        return True
   
    
def my_func1(x, y):
    result = x ** y
    return result


def my_func2(x, y):
    result_znam = 1
    for _ in range(abs(y)):
        result_znam *= x
    result = 1 / result_znam
    return result


while True:    
    arg1 = input("Введи первое  действительное положительное число: ")
    if is_valid_decimal(arg1):
        if float(arg1) > 0:
            break
        else:
            print("Введи только действительное положительное число, Товарищ пользователь")
            
arg1 = float(arg1)

while True:    
    arg2 = input("Введи второе целое отрицательное число: ")
    if is_valid_int(arg2):
        if int(arg2) < 0:
            break
        else:
            print("Введи только целое отрицательное число, Товарищ пользователь")
arg2 = int(arg2)

print(f"Результат возведения в степень первого числа на второе: {my_func1(arg1,arg2)}")
print(f"Результат возведения в степень первого числа на второе: {my_func2(arg1,arg2)}")
