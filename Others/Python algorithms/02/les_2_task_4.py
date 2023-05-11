# Created by Nikolay Pakhomov 10.05.2023

# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры.

def geom_progression(n):
    q = -0.5
    b = 1
    return b * (q ** n - 1) / (q - 1)


print(geom_progression(1))
print(geom_progression(2))
print(geom_progression(4))
print(geom_progression(10000))
