# Created by Nikolay Pakhomov 24.05.2023

import cProfile


# Проверка функции
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f"Test {i} OK")


# Вариант 2. Рекурсия + словарь.
def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


# test_fib(fib_dict)

# timeit:
# python -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(10)"
# 1000 loops, best of 5: 2.93 usec per loop
# python -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(15)"
# 1000 loops, best of 5: 4.16 usec per loop
# python -m timeit -n 1000 -s "import task_4" "task_4.fib_dict(20)"
# 1000 loops, best of 5: 5.51 usec per loop
# Работает быстрее.


# cProfile:
cProfile.run('fib_dict(10)')
# 19/1    0.000    0.000    0.000    0.000 task_4.py:18(_fib_dict) 10
# 39/1    0.000    0.000    0.000    0.000 task_4.py:18(_fib_dict) 20

# Вывод: Время выполнения увеличивается пропорционально с ростом 'n', также растет и количество вызовов функции.
