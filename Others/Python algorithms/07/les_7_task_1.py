# Created by Nikolay Pakhomov 19.07.2024
# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

LST_LEN = 10
random_lst = [random.randint(-100, 99) for i in range(LST_LEN)]


def bubble_sort(numb_arr):
    a = numb_arr

    len_arr = len(a)
    for i in range(len_arr - 1):
        counter = 0
        for j in range(len_arr - 1 - i):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                counter += 1
        if counter == 0:
            break
    return a


print(f'Исходный массив:\n{random_lst}\n')
print(f'Сортированный массив:\n{bubble_sort(random_lst)}')
