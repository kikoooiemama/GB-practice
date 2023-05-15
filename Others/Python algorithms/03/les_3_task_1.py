# Created by Nikolay Pakhomov 15.05.2023

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

natural_nums = [_ for _ in range(2, 100)]
counter = [0] * 8

# 2, 3, 5, 7 - простые числа от 2 до 9
for n in natural_nums:
    if n % 2 == 0:
        counter[0] += 1
        if n % 4 == 0:
            counter[2] += 1
            if n % 8 == 0:
                counter[6] += 1
        if n % 6 == 0:
            counter[4] += 1
    if n % 3 == 0:
        counter[1] += 1
        if n % 9 == 0:
            counter[7] += 1
    if n % 5 == 0:
        counter[3] += 1
    if n % 7 == 0:
        counter[5] += 1

# вывод
print("Делители:          ", end='')
for m in range(2, 10):
    print(f"{m:>3}", end=' ')
print("\nКоличество кратных:", end='')
for i in range(8):
    print(f"{counter[i]:>3}", end=' ')
