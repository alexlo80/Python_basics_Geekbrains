"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы 
складываем с первым элементом первой строки второй матрицы и т.д."""

class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __add__(self, other):

        while len(self.list_1) != len(other.list_1):
            other.list_1.append([]) if len(self.list_1) > len(other.list_1) else self.list_1.append([])
        for i in range(len(self.list_1)):
            while len(self.list_1[-i]) != len(other.list_1[-i]):
                other.list_1[-i].append(0) if len(self.list_1[-i]) > len(other.list_1[-i]) else self.list_1[-i].append(0)
        matr = [[0 for q in range(len(other.list_1[0]))]for i in range(len(self.list_1))]
        for i in range(len(self.list_1)):
            for j in range(len(other.list_1[i])):
                matr[i][j] = self.list_1[i][j] + other.list_1[i][j]

        return Matrix(matr)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]))


if __name__ == "__main__":
    my_matrix1 = Matrix([[5, 18, 11],
                        [6, 17, 23],
                        [41, 50, 9]])
    my_matrix2 = Matrix([[45, 8, 2],
                        [6, 7, 93]])

    print(my_matrix1 + my_matrix2)
