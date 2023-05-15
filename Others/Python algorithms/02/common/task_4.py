# Created by Nikolay Pakhomov 10.05.2023
# Рекурсия
def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'


print(func(1, 10))
print(func(10, 2))
# Помним о maximum recursion depth
