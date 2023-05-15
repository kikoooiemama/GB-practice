# Created by Nikolay Pakhomov 15.05.2023

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.
import random

size = 15
a = 1
b = 20
random_arr = [random.randint(a, b) for _ in range(size)]
print(random_arr)

i_min, i_max = 0, 0
x_min, x_max = random_arr[i_min], random_arr[i_max]
for i in range(size):
    if random_arr[i] > x_max:
        x_max = random_arr[i]
        i_max = i
    if random_arr[i] < x_min:
        x_min = random_arr[i]
        i_min = i

result = 0
inc = 1 if i_min < i_max else -1
for num in random_arr[i_min + inc:i_max:inc]:
    result += num
print(f"Сумма между минимальным и максимальным значением: {result}")
