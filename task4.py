"""4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

user_reply_n = input("please insert number n: ")
if user_reply_n.isdigit():
    number = int(user_reply_n)
    biggest_number = 0
    while number:
        n = number % 10
        if biggest_number < n:
            biggest_number = n
        number //= 10
    print("самая большая цифра в числе :", biggest_number)
else:
    print("insert just numbers!!")
