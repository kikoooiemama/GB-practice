# Created by Nikolay Pakhomov 27.02.2025
# Быстрая сортировка (Хоара)
# 1. Выбираем опорный элемент (pivot)
# 2. Сравниваем элементы массива с опорным и переставляем их так, чтобы разбить массив на три непрерывных отрезка:
# "меньшие опорного", "равные" и "большие".
# 3. Для отрезков меньше и больше рекурсивно выполнить сортировку.


import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []
    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception("Случилось непредвиденное")

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


def quick_sort_short(array):
    if len(array) < 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort_short(less) + [pivot] + quick_sort_short(greater)


# print(quick_sort_short(array))
print(quick_sort(array))
