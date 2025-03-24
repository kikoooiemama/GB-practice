# Created by Nikolay Pakhomov 27.02.2025
# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.

import random

LST_LEN = 5
lst = [random.randint(0, 100) for _ in range(2 * LST_LEN + 1)]


def median(lst):
    k = 0
    min_val = min(lst)
    max_val = max(lst)

    while True:

        min_lst = 0
        max_lst = 0
        var = lst[k]

        if min_val <= var <= max_val:
            for i in lst:
                if i <= var:
                    min_lst += 1
                if i >= var:
                    max_lst += 1

        if min_lst == max_lst != 0:
            return var
        elif min_lst > max_lst:
            max_val = var
        elif min_lst < max_lst:
            min_val = var

        if len(lst) - 1 > k:
            k += 1
        else:
            return max_val


# Гномья сортировка
def gnome_sort(lst):
    i = 1
    while i < len(lst):

        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
            if i == 0:
                i = 1

    return lst


print(f'Исходный массив:\n{lst}')
print(f'Медиана по гномьей сортировке: {gnome_sort(lst)[len(lst) // 2]}')
print(f'Медиана по моей сортировке: {median(lst)}')
