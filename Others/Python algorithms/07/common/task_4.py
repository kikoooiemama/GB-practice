# Created by Nikolay Pakhomov 27.02.2025
# Сортировка Шелла (вставки, - память)
# 1. Выбираем шаг для сравнения элементов (increment)
# 2. Сравниваем последовательно элементы массива находящиеся один от другого на расстоянии шага
# 3. Уменьшаем шаг и повторяем пункт два.

# Топ шаги (до 4000 элементов в массиве): 1, 4, 10, 23, 57, 132, 301, 701, 1750

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def shell_sort(array):
    assert len(array) < 4000

    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]


shell_sort(array)
print(array)
