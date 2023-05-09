# Created by Nikolay Pakhomov 04.05.2023

# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input("Введите 1-е число: "))
b = float(input("Введите 2-е число: "))
c = float(input("Введите 3-е число: "))
m = a
if m > b:
    if m > c:
        if c > b:
            m = c
        else:
            m = b
else:
    if m < c:
        if c > b:
            m = b
        else:
            m = c
print(f"\nСреднее число: {m}")
