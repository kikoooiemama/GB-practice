# Created by Nikolay Pakhomov 15.05.2023

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
# значения.
import random

size = 20
a = -5
b = 5
random_arr = [random.randint(a, b) for _ in range(size)]
print(random_arr)

result = a - 1
result_idx = -1

for i in range(size):
    if 0 > random_arr[i] > result:
        result = random_arr[i]
        result_idx = i

if result_idx == -1:
    print("В массиве нет отрицательных чисел!")
else:
    print(f"Максимальное отрицательное число: {result}\nПозиция: {result_idx}")
