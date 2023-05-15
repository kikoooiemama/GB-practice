# Created by Nikolay Pakhomov 15.05.2023

# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.
import random

a = 5
b = 4
matrix = []
for i in range(a):
    print(f"Введите {i+1} строку: ")
    line = [float(input(f"Введите элемент {j+1}:")) for j in range(b - 1)]
    line_sum = 0
    for n in line:
        line_sum += n
    line.append(line_sum)
    matrix.append(line)
print()
for line in matrix:
    for item in line:
        print(f'{item:>6}', end='')
    print()