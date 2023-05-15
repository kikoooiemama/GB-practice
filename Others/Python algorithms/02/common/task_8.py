# Created by Nikolay Pakhomov 10.05.2023
# Функция перевода десятичного числа в двоичный формат

def binary(num):
    s = ''
    while num > 0:
        s = f'{(num % 2)}{s}'
        num //= 2
    return s


# print(binary(10))
# print(binary(255))

while True:
    n = int(input('Введите целое число: '))
    if n != 0:
        print(binary(n))
    else:
        break
