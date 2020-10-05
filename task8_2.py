"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class Division:
    def __init__(self, param1, param2):
        self.divider = param1
        self.denominator = param2

    @staticmethod
    def divide_by_null(param1, param2):
        try:
            return param1 / param2
        except:
            return f"Деление на ноль недопустимо!"
        
if __name__ == '__main__':
    
div = Division(10, 100)
print(Division.divide_by_null(10, 0))
print(Division.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
