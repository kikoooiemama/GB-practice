# Created by Nikolay Pakhomov 15.05.2023

import random

# Разложить положительные и отрицательные числа по разным массивам.
array = [random.randint(-100, 100) for _ in range(100)]
print(array)

arr_below = []
arr_larger = []

for item in array:
    if item > 0:
        arr_larger.append(item)
    elif item < 0:
        arr_below.append(item)

print(arr_below)
print(arr_larger)

# Так лучше чем 2 генератора. Там будет 2n обход.
