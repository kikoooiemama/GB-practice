# Created by Nikolay Pakhomov 24.05.2023
import cProfile


def get_len(array):
    return len(array)


def get_sum(array):
    s = 0
    for i in array:
        s += i
    return s


def main():
    lst = [i for i in range(100000000)]
    a = get_len(lst)
    b = get_sum(lst)


# результат будет в секундах!
cProfile.run('main()')
