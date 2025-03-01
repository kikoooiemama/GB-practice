# Created by Nikolay Pakhomov 12.02.2025
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел
# из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import defaultdict
from collections import deque


def to_dec(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def to_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = to_dec(input('Введите первое число в шестнадцатеричном формате: ').upper())
num_2 = to_dec(input('Введите второе число в шестнадцатеричном формате: ').upper())

print(f'Сумма чисел: {to_hex(num_1 + num_2)}')
print(f'Произведение чисел: {to_hex(num_1 * num_2)}')
