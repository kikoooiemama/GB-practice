# Created by Nikolay Pakhomov 10.05.2023

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def num_sequence(numbers):
    n_numbers = int(input("Введите количество чисел: "))
    c = int(input("Введите цифру: "))
    res = 0
    if len(numbers) < n_numbers:
        n_numbers = len(numbers)
    for i in range(n_numbers):
        num = numbers[i]
        while num > 0:
            if c == num % 10:
                res += 1
            num //= 10
    return res


seq = [123, 6348, 834510, 77, 73, 98, 91, 547, 83]
print(num_sequence(seq))
