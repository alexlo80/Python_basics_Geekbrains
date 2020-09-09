"""5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

user_reply_turnover = input("Введите значения выручки: ")
if user_reply_turnover.isdigit():
    user_reply_cost = input("Введите значения издержек фирмы: ")
    if user_reply_cost.isdigit():
        profit = int(user_reply_turnover) - int(user_reply_cost)
        if profit >= 0:
            print("Контора с прибылью : ", profit)
            print("Рентабельность : ", profit / int(user_reply_turnover))
        else:
            print("Контора с убытком : ", profit)
        qty = input("Сколько трудяг в фирме? ")
        if qty.isdigit():
            print("На каждую душу приходится прибыли :", profit/int(qty))
        else:
            print("insert just numbers!!")
    else:
        print("insert just numbers!!")
else:
    print("insert just numbers!!")
