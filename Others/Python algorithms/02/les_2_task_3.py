# Created by Nikolay Pakhomov 10.05.2023

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, надо вывести 6843.

def flip_num(num):
    res = 0
    while num > 0:
        digit = num % 10
        num //= 10
        res *= 10
        res += digit
    return res


print(flip_num(3486))
