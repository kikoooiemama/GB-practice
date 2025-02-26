# Created by Nikolay Pakhomov 13.02.2025

from count_mem_size import count_size


def var_sum(var_lst):
    summa = 0
    for i in var_lst:
        summa += count_size(i)
    print(f'Под переменные задействовано {summa} байт памяти.')


# Ввод данных.
n = int(input('Введите n: '))

# Алгоритм №1.
sum_ = 0
for j in range(n):
    sum_ += (-1) ** j / 2 ** j
var_sum([sum_, j])

# Алгоритм №2.
item = 1
summ = 0
for _ in range(n):
    summ += item
    item /= -2
var_sum([item, summ, _])

# Алгоритм №3.
summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
var_sum([summa_2])

# Результат:
# №1. Под переменные задействовано 52 байт памяти.
# №2. Под переменные задействовано 76 байт памяти.
# №3. Под переменные задействовано 24 байт памяти.
# Очевидно, что по памяти эффективнее программа с одной переменной.
