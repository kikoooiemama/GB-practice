# Created by Nikolay Pakhomov 27.02.2025
# Разворот массива.
# Сортировка Python - используется Timsort (2002 год).
# Использует вставку + Слияние. Сложность O(n log n)
# Потребляет память O(n)

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]


revers(array)
print(array)

array.reverse()
print(array)

array.sort()
print(array)

array.sort(reverse=True)
print(array)

print('*' * 50)
t = tuple(random.randint(0, 100) for _ in range(size))
print(t)

t = tuple(sorted(t, revers=True))
print(t)
