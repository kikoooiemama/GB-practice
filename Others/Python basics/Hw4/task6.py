# Реализовать два небольших скрипта:
#     *итератор, генерирующий целые числа, начиная с указанного;
#     *итератор, повторяющий элементы некоторого списка, определённого заранее.

# Чтоб разобраться между итераторами и генераторами и не путать их:
# https://tirinox.ru/gen-and-iter/
# https://www.alexkorablev.ru/2016/02/29/generator-vs-iterator/
# https://pythoner.name/list-generator

# https://docs.python.org/3/library/itertools.html#itertools.islice
# itertools.islice(iterable, [start], stop[, step]) -> iterator - возвращает итератор по ограниченному подмножеству
# элементов переданного объекта. В отличие от обычных срезов, данная функция не поддерживает отрицательные значения
# в start, stop, step.

from itertools import cycle
from itertools import count
from itertools import islice


def generate(begin, end):
    try:
        generator_list = [num for num in islice(count(), int(begin), int(end) + 1)]
        print(generator_list)
    except ValueError:
        print("Ошибка! Введены не числа, или значение begin и end < 0, или begin > end!")


def repeat(iter_list, iter_num):
    try:
        repeat_list = [s for s in islice(cycle(iter_list), int(iter_num))]
        print(repeat_list)
    except ValueError:
        print("Ошибка! Неккоректное значение количества повторов.")


print("Приветствую, пользователь!")
print(f"Введите данные для 1-го скрипта.")
generate(input("Введите число, с которого начнется итератор: \n"),
         input("Введите число, на котором закончится итератор: \n"))

print(f"Введите данные для 2-го скрипта.")
iter_str = "ABC123"
repeat(iter_str, input("Введите количество итераций: \n"))
