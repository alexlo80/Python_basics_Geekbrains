"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def accept_divide(first, second):
    global result 
    result = None
    try: 
        result = first/second
    except ZeroDivisionError:
        print("Деление на 0 запрещено")
    return result


while True:    
    first = input("Введи первое число: ")
    second = input("Введи второе число: ")
    if first.isdigit() and second.isdigit():
        first, second = int(first), int(second)
        break
    else:
        print("Введи только числа, Товарищ пользователь")
        
accept_divide(first, second)        
print(f"Результат деления первого числа на второе : {result}")
