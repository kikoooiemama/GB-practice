# Created by Nikolay Pakhomov 15.05.2023

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба минимальны), так и различаться.
import random

size = 15
a = 1
b = 20
random_arr = [random.randint(a, b) for _ in range(size)]
print(random_arr)

x_min, x_min_ = b + 1, b + 1
for i in range(size):
    if random_arr[i] < x_min:
        x_min_ = x_min
        x_min = random_arr[i]
    elif random_arr[i] < x_min_:
        x_min_ = random_arr[i]

print(f"Два наименьших элемента: {x_min}, {x_min_}")
