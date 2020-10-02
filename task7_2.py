"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Textil(ABC):
    
    @abstractmethod
    def my_method_1(self):
        pass

    def __init__(self, size):
        self.size = size

    @property
    def get_square_c(self):
        return round(self.size / 6.5 + 0.5)
    
    @property
    def get_square_j(self):
        return round(self.size * 2 + 0.3)

    def __add__(self, other):
        total = self.get_square_c + other.get_square_j
        return f'Площадь ткани на все: {total}'
    
    
class Coat(Textil):
    def __init__(self, size):
        super().__init__(size)
   
    def my_method_1(self):
        print("Считаю размер ткани на пальто")


class Jacket(Textil):
    def __init__(self, size):
        super().__init__(size)
        
    def my_method_1(self):
        print("Считаю размер ткани на костюм")

        
if __name__ == "__main__":
    coat = Coat(4)
    jacket = Jacket(2)

coat.my_method_1()
print(coat.get_square_c)
jacket.my_method_1()
print(jacket.get_square_j)
print(coat+jacket)
