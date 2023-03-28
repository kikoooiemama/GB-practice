# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.

# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
from random import random
from random import randint

print("Приветствую, пользователь!")
source_list = [round(random() * 1000, 1) for number in range(1, randint(10, 20))]
result_list = [number for index, number in enumerate(source_list[1:]) if number > source_list[index]]
print(f"Исходный список: {source_list}")
print(f"Результат:       {result_list}")
