import random


# функция бросания фишек в одном раунде
def AnotherTurn(dies_qty, turnsD, new_dies, player):
    # все возможные варианты фишек в зависимости от цвета фишек
    colors = {'green': ['brain', 'brain', 'brain', 'away', 'away', 'shot'],
        'yellow': ['brain', 'brain', 'shot', 'away', 'away', 'shot'],
        'red': ['brain', 'shot', 'shot', 'away', 'away', 'shot']}
    # общее количество фишек на старте раунда
    dies_qty = ['green', 'green', 'green', 'green', 'green', 'green', 'yellow', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red']

    turnsD = []
    result1turn = []
    resulttotalplayer1 = []
    resultround = []
    countshts = 0
    countbrains = 0
    countaway = 0
    summ = 0

# Цикл продолжается, пока игрока не подстрелят 3 раза
    while countshts < 3:
        turnsA = []
        if new_dies != 0: # не нужно брать новые фишки если у тебя на руках 3 "away"
            for i in range(new_dies):
                c =random.randint(0,len(dies_qty)-1)  # рандомный выбор фишки
                turnsD.append(dies_qty[c])
                del dies_qty[c]  # количество фишек в банке должно уменьшаться
                c = ''
        for i in turnsD:
            turnsA.append(i+"-"+colors[i][random.randint(0,5)])  # рандомный выбор события с фишки
        turnsD = []
        countshtsturn = 0
        countbrainsturn = 0
        countawayturn = 0
        for z in turnsA:  # подсчет выпавших событий
            if "shot" in z:
                countshts += 1  #выстрелы переходят внутри раунда из попытки в попытку
                countshtsturn += 1
            elif "brain" in z:
                countbrainsturn += 1
            elif "away" in z:
                countawayturn += 1

        if countawayturn > 0 and countawayturn < 3:  # подсчет сколько фишек надо перебрасывать в очередной попытке
            new_dies = 3-countawayturn
        elif countawayturn == 0:
            new_dies = 3
        elif countawayturn == 3:
            new_dies = 0

        for i in turnsA:  # определение какие фишки мы будем повторно перебрасывать
            if i.endswith("away"):
                turnsD.append(i.split('-')[0])
        print()
        print(f'Now is playing player {player}')
        #print(';'.join(turnsA))

        for i in turnsA:  # разноцветная печать выпавших фишек
            if 'green' in i:
                print('\033[32m'+i)
            elif 'yellow' in i:
                print('\033[33m'+i)
            else:
                print('\033[31m'+i)

        if countshts >= 3:  # что делать если игрока подстрелили более 3х раз
            print()
            print('\033[31m'+'This roud is over for you! You have got 3 shots.')
            result1turn = 0
            resultround.clear()  # результаты раунда обнуляются
            resultsOfGame[player] += sum(resultround)  # подсчет итоговых результатов игры
            print('\033[30m'+f'''Result of the game of player №{player} is {resultsOfGame[player]}''')
            c = input('\033[36m'+'Another player, are you ready for your turn?')
            break
        else:
            result1turn = countbrainsturn - countshtsturn  # подсчет результатов раунда и вывод на печать
        resultround.append(result1turn)
        print('\033[30m'+f'''Result of this turn is:{result1turn}.
You have got already {countshts} shots.
Total round result is {sum(resultround)}''')


        if countshts < 3 and new_dies < 3:  # что делать если игрока подстрелили менее 3х раз и есть возможность перебросить фишки
            answer = input('\033[30m'+"Would you like another turn (y/n)?")
            if answer == 'n':
                resultsOfGame[player] += sum(resultround)  # подсчет итоговых результатов игры
                print('\033[30m'+f'Result of the game of player №{player} is {resultsOfGame[player]}')
                if resultsOfGame[1] < 13 and resultsOfGame[2] < 13:  # запрос на продолжение игры другим игроком(просто пауза)
                    c = input('\033[36m'+'Another player, are you ready for your turn?')
                break
        else:
            resultsOfGame[player] += sum(resultround)  # подсчет итоговых результатов игры
            print('\033[30m'+f'Result of the game of player №{player} is {resultsOfGame[player]}')
            if resultsOfGame[1] < 13 and resultsOfGame[2] < 13:  # запрос на продолжение игры другим игроком(просто пауза)
                c = input('\033[36m'+'Another player, are you ready for your turn?')
            break


dies_qty = []
turnsD = []
new_dies = 0

resultsOfGame = {1:0,2:0}  # подсчет результатов игры в словаре
player = 2


while resultsOfGame[1] < 13 and resultsOfGame[2] < 13:  # функция будет запускаться пока один из игроков не наберет 13
    if player == 2:  # смена игроков
        player = 1
    else:
        player = 2
    AnotherTurn(dies_qty, turnsD, 3, player)  # запуск функции одного раунда

print(f'The winner is Player {player} with a rusult of {resultsOfGame}')
