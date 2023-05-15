# Created by Nikolay Pakhomov 15.05.2023

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

a = 5
b = 4
up_th = 10
bottom_th = 1
matrix = [[random.randint(bottom_th, up_th) for _ in range(b)] for _ in range(a)]
# вывод
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print()

# поиск минимальных элементов каждого столбца
min_column = [up_th] * len(matrix[0])
for line in matrix:
    for i in range(len(line)):
        if min_column[i] > line[i]:
            min_column[i] = line[i]

for s in min_column:
    print(f'{s:>4}', end='')
# поиск максимального из минимальных
result = 0
for num in min_column:
    if num > result:
        result = num

print(f"\n\nМаксимальный элемент среди минимальных элементов столбцов матрицы: {result}")
