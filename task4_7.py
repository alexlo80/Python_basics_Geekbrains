def fact(n):
    """
    Фукнция вычисляет факториал и на каждом шаге вычисления дает управление программе
    :param n: 
    :return: 
    """
    total = 1
    for el in range(1, n+1):
        total *= el
        yield total


for el in fact(6):     
    print(el)
