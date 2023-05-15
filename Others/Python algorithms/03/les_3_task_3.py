# Created by Nikolay Pakhomov 15.05.2023

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

size = 15
a = -25
b = 25
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

random_arr[i_max] = x_min
random_arr[i_min] = x_max

print(random_arr)
