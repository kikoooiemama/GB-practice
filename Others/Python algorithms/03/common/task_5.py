# Created by Nikolay Pakhomov 15.05.2023

import random

# Обмен значений главной и побочной диагоналей квадратной матрицы
size = 5
matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print()

for i in range(size):
    for j in range(size):
        if i == j:
            spam = matrix[i][j]
            matrix[i][j] = matrix[i][size - 1 -j]
            matrix[i][size - 1 - j] = spam

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print()