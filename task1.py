"""1.Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в
переменные, выведите на экран."""

# Поработайте с переменными, создайте несколько, выведите на экран
perem_str = "Text variable"
perem_int = 12345
perem_float = 3.1415
perem_bool = True
print(f"str: {perem_str}, int: {perem_int}, float: {perem_float},bool:{perem_bool}")
print()

# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран
user_reply_num = input("please insert number: ")
if user_reply_num.isdigit():
    user_reply_str = input("please insert text: ")
else:
    print("please insert just numbers!!")
print(int(user_reply_num) * user_reply_str)
print()

# вывод в столбик
number = int(user_reply_num)
while number:
    print(user_reply_str)
    number -= 1
© 2020 GitHub, Inc.
