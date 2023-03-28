# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить её на экран.
from random import random
from random import randint

# Как я понял. Нужно записать в файл числа, потом считать эти числа из файла и найти их сумму.
try:
    with open("text_5.txt", "w+", encoding="utf-8") as f:
        numbers = [str(round(random() * 100, 2)) for n in range(10, randint(15, 25))]
        f.write(" ".join(numbers))
        f.seek(0)
        read_numbers = list(map(float, f.read().split()))
        print(f"Числа из файла: {read_numbers}")
        print(f"Сумма чисел в файле: {round(sum(read_numbers), 2)}")
except IOError as err:
    print("IOError: Ошибка при открытии/чтении/записи файла\n", err)
except ValueError as err:
    print("ValueError: Ошибка при чисел из файла\n", err)
