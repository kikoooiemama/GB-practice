# Created by Nikolay Pakhomov 15.05.2023

# 4. Определить, какое число в массиве встречается чаще всего.
import random

size = 15
a = 1
b = 5
random_arr = [random.randint(a, b) for _ in range(size)]
print(random_arr)
counter = {}
# посчитали
for num in random_arr:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

# нашли самое частое число
max_n = 0
ans = 0
for k, v in counter.items():
    if v > max_n:
        ans = k
        max_n = v
# вывод
print(ans)
