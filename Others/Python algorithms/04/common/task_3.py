# Created by Nikolay Pakhomov 24.05.2023

import cProfile
import functools


# Проверка функции
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f"Test {i} OK")


# Вариант 1. Рекурсивная реализация.
@functools.lru_cache()  # декоратор для функции: мемоизация результата
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Тест
# test_fib(fib)
# python -m timeit -n 1000 -s "import task_3" "task_3.fib(10)"
# 1000 loops, best of 5: 14.8 usec per loop
# 1000 loops, best of 5: 59.3 nsec per loop - с декоратором
# cProfile.run("fib(20)")

# Экспоненциальная сложность алгоритма.

# рекурсия это плохо - экспоненциальная сложность и ограничение на количество вызовов функции
# цикл - оптимально.
