"""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def print_oneline(name, last_name, year, email, phone):
    print(name, last_name, year, email, phone)


print_oneline(name=input("Имя: "), last_name=input("Фамилия: "),
              year=input("Год рождения: "), email=input("email: "), phone=input("Телефон: "))
