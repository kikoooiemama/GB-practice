# Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел,
# соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения задания
# обязательно используйте генератор.

# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
from random import random
from random import randint

print("Приветствую, пользователь!")
source_list = [int(random() * 15) for number in range(1, randint(10, 20))]
result_list = [el for el in source_list if source_list.count(el) == 1]
print(f"Исходный список: {source_list}")
print(f"Результат:       {result_list}")
