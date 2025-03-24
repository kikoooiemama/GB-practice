# Created by Nikolay Pakhomov 27.02.2025
# Сортировка вставками
# 1. Из массива последовательно берется каждый элемент, кроме idx = 0
# 2. И вставляется в отсортированную часть массива.

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

        array[j] = spam


insertion_sort(array)
print(array)
