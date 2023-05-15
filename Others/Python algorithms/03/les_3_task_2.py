# Created by Nikolay Pakhomov 15.05.2023

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
import random

size = 10
first_arr = [random.randint(1, 15) for _ in range(size)]
print(first_arr)
second_arr = []
for i in range(size):
    if first_arr[i] % 2 == 0:
        second_arr.append(i)

print(f"Индексы четных элементов: ")
print(second_arr)
