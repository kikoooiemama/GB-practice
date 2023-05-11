# Created by Nikolay Pakhomov 10.05.2023

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count_nums(num):
    even = 0
    odd = 0
    while num > 0:
        a = num % 10
        num //= 10
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"Четных: {even}, Нечетных: {odd}"


print(count_nums(34560))
print(count_nums(555555))