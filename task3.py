"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

user_reply_n = input("please insert number n: ")
if user_reply_n.isdigit():
    number = int(user_reply_n)
    # first option to  calculate sum
    # summa = number + (number*10+number) + ((number*10+number)*10+number)

# second option with while loop
    i = 3
    n = 0
    nn = number
    while i:
        n += nn
        nn = nn * 10 + number
        i -= 1
    print("sum({0}+{0}{0}+{0}{0}{0}) = ".format(number), n)
else:
    print("insert just numbers!!")
