"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""


while True:
    user_input = input("Введите номер месяца (1-12):")
    if user_input.isdigit():
        month = int(user_input)
        break
    else:
        print("Введите число!")

# через словарь
my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",
           7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
season = my_dict.get(month)
print(f"Этот месяц относится к сезону: {season}")

# через список
my_list = list(my_dict.values())
try:
    season = my_list[month-1]
except IndexError:
    print("Oops!  That was no valid number.  Try again...")
print(f"Этот месяц относится к сезону: {season}")