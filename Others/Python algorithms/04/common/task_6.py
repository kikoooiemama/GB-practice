# Created by Nikolay Pakhomov 24.05.2023
import cProfile


# Проверка функции
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f"Test {i} OK")


# Вариант 4. Нерекурсивный поиск чисел Фибоначчи.

def fib_loop(n):
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second


test_fib(fib_loop)
# python -m timeit -n 1000 -s "import task_6" "task_6.fib_dict(100)"
cProfile.run('fib_loop(100000)')
