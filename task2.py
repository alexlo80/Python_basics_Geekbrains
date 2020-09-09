"""2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

user_reply_seconds = input("please insert number of seconds: ")
if user_reply_seconds.isdigit():
    number = int(user_reply_seconds)
    hours = number // 3600
    minutes = number % 3600 // 60
    seconds = number % 3600 % 60
    print("%02d:%02d:%02d" % (hours, minutes, seconds))
else:
    print("insert just numbers!!")
