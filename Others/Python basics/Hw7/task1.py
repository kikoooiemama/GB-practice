# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для формирования матрицы.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        max_value = max(list([len(str(number)) for rows in self.matrix for number in rows]))
        return "\n".join(map(lambda numbers_list: "   ".join(
            map(lambda number: "{:>{x}}".format(str(number), x=max_value), numbers_list)), self.matrix))

    def __add__(self, other):
        result_list = list(
            map(lambda number_list_1, number_list_2: list(map(lambda x, y: x + y, number_list_1, number_list_2)),
                self.matrix, other.matrix))
        return Matrix(result_list)


matrix_1 = Matrix([list(range(1, 6, 2)), list(range(1, 4)), list(range(2, 7, 2))])
matrix_2 = Matrix([[1111, 2, 3, ], [4, 2, 6], [1, 2, -809]])
print(f"First matrix:\n{matrix_1}\n")
print(f"Second matrix:\n{matrix_2}\n")
matrix__ = matrix_1 + matrix_2
print(f"Sum matrix:\n{matrix__}")
