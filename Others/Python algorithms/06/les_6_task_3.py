# Created by Nikolay Pakhomov 13.02.2025

from count_mem_size import count_size

x1 = float(input('Введите координату X первой точки: '))
y1 = float(input('Введите координату Y первой точки: '))
x2 = float(input('Введите координату X второй точки: '))
y2 = float(input('Введите координату Y второй точки: '))
if x2 == x1:
    print('Error')
    exit()
k = (y2 - y1) / (x2 - x1)
b = (y1 - k * x1)
if b == 0:
    print(f'Уравнение прямой y = {k: .2f}x')
elif b > 0:
    print(f'Уравнение прямой y = {k: .2f}x + {b:.2f}')
else:
    print(f'Уравнение прямой y = {k: .2f}x - {abs(b): .2f}')

sum_ = 0
var_lst = (x1, y1, x2, y2, k, b)
for i in var_lst:
    sum_ += count_size(i)
print()
print(f'Под переменные задействовано {sum_} байт памяти')
# Под переменные задействовано 144 байт памяти.
