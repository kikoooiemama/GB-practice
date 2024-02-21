# Created by Nikolay Pakhomov 24.05.2023
import timeit

x = 2 + 2
print(timeit.timeit('x=2+2'))
print(timeit.timeit('x = sum(range(10))'))
# python -m timeit -n 100 "import task_1"
