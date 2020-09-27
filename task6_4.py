"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
 остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
 превышении скорости.Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажитерезультат."""

import random
direction = {0: "на лево", 1: "на право"}


class Car:
    def __init__(self, speed, color="black", name="blabla", is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def stop(self):
        if self.speed == 0:
            print("Машина стоит")
        else:
            print("Машина не стоит")

    def go(self):
        if self.speed > 0:
            print("Машина едет")
        else:
            print("Машина не едет")

    def turn(self):
        print(f"Машина повернула {direction[random.randint(0,1)]}")

    def show_speed(self):
        print(f"Скорость машины {self.speed}")


class TownCar(Car):

    def show_speed(self):
        print(f"Скорость машины {self.speed}")
        if self.speed > 60:
            print("Вы превысили скорость!")


class SportCar(Car):
     def printid(self):
        print("I am sport car")


class WorkCar(Car):

    def show_speed(self):
        print(f"Скорость машины {self.speed}")
        if self.speed > 40:
            print("Вы превысили скорость!")


class PoliceCar(Car):

    def printabout(self):
        print('я из полиции')


car1 = TownCar(78)
car1.show_speed()
car1.go()
car1.turn()
car1.stop()

car2 = WorkCar(45)
car2.show_speed()
car2.go()
car2.turn()
car2.stop()

audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)

lada.show_speed()
print(lada.color)
