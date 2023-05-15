# Created by Nikolay Pakhomov 10.05.2023

# import sys
# sys.setrecursionlimit(3000)

# Функция Аккермана
def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


print(akk(1, 1))
print(akk(2, 4))
print(akk(3, 4))
