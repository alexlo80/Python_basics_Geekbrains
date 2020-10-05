"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class Store:
    pass


class Org:

    def __init__(self, name,  quantity):
        self.name = name
        self.quantity = quantity

        
class Printer(Org):
    def __init__(self, name, quantity, pages):
        super().__init__(name, quantity)
        self.numb = pages
        
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Org):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity)
        self.price = price
        
    def to_scan(self):
        return f' Price of scanner is {self.price}'


class Xerox(Org):
    def __init__(self, name, quantity, resolution):
        super().__init__(name, quantity)
        self.resolution = resolution
        
    def to_copy(self):
        return f'to copy  with resolution of  {self.resolution}'


unit_1 = Printer('hp', 5, 2000)
unit_2 = Scanner('Canon', 5, 100)
unit_3 = Xerox('Xerox', 1, 600)
print(unit_1.to_print())
print(unit_3.to_copy())
print(unit_2.price)

