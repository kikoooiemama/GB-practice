# Реализовать программу работы с органическими клетками, состоящими из ячеек.

class Cell:
    def __init__(self, subcells):
        self.subcells = subcells

    def make_order(self, rows):
        return "\n".join(["*" * rows for _ in range(self.subcells // rows)]) + "\n" + "*" * (self.subcells % rows)

    def __str__(self):
        return f"Клетка: {self.subcells} яч."

    # Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    def __add__(self, other):
        return Cell(self.subcells + other.subcells)

    # Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить
    # соответствующее сообщение.
    def __sub__(self, other):
        return Cell(abs(self.subcells - other.subcells)) if abs(self.subcells - other.subcells) != 0 \
            else "Вычитание невозможно!"

    # Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
    # двух клеток.
    def __mul__(self, other):
        return Cell(self.subcells * other.subcells)

    # Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек
    # этих двух клеток.
    def __floordiv__(self, other):
        return Cell(self.subcells // other.subcells)


cell_1 = Cell(73)
print(cell_1.make_order(5))

cell_1 = Cell(19)
cell_2 = Cell(7)
print(f"\nСуммирование\n{cell_1 + cell_2}\n")

cell_1 = Cell(19)
cell_2 = Cell(7)
print(f"Вычитание\n{cell_1 - cell_2}\n")

cell_1 = Cell(4)
cell_2 = Cell(27)
print(f"Вычитание\n{cell_1 - cell_2}\n")

cell_1 = Cell(4)
cell_2 = Cell(4)
print(f"Вычитание\n{cell_1 - cell_2}\n")

cell_1 = Cell(19)
cell_2 = Cell(7)
print(f"Умножение\n{cell_1 * cell_2}\n")

cell_1 = Cell(19)
cell_2 = Cell(7)
print(f"Деление\n{cell_1 // cell_2}\n")
