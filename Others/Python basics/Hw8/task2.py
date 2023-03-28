# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


print("Программа, реализующая действие 'деление'.\n"
      "'a / b', где a - делимое, b - делитель.")
a = input("Введите делимое (a):\n")
b = input("Введите делитель (b):\n")
try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise MyZeroDivisionError("Деление на 0 запрещено!")
    result = a / b
except ValueError:
    print("Вы ввели не число!")
except MyZeroDivisionError as err:
    print(err)
else:
    print(f"Результат деления: {round(result, 3)}")
