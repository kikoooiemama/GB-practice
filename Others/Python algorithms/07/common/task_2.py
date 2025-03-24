# Created by Nikolay Pakhomov 27.02.2025
# Сортировка выбором.
# 1. Находим наименьший элемент в неотсортированной части массива.
# 2. Поменять его местами с первым элементом в неотсортированной части массива
# 3. Продолжать пока не отсортируем.

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selection_sort(array):
    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]


selection_sort(array)
print(array)
