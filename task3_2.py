"""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""
# простой вариант
#def print_oneline(name, last_name, year, email, phone):
 #   print(name, last_name, year, email, phone)


#print_oneline(name=input("Имя: "), last_name=input("Фамилия: "),
 #             year=input("Год рождения: "), email=input("email: "), phone=input("Телефон: "))

# вариант с проверкой форматов
def print_oneline(i):
    """
    Функция делает распечатку словаря. Выводит только значения.
    :param i: 
    :return: 
    """
    for v in info.values():
        print(v, end=" ")


info = {}
info_template = {"name": ("Имя товарища", str), "last_name": ("Фамилия: ", str), 
               "year": ("Год рождения: ", int), "email": ("email: ", str), 
               "phone": ("Телефон: ", int)}

for k, v in info_template.items():
    while True:
        user = input(f'{v[0]}\n')
        try:
            user = v[1](user)
        except ValueError as e:
            print(f"Не верное значение данных")
            continue
        info[k] = user
        break
        
print_oneline(info)   
