# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.


class MyNoNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_non_positive_number(input_number):
    count_of_dots = input_number.count(".")
    if count_of_dots == 1:
        split_number = input_number.split(".")
        if not (split_number[0].isdigit() and split_number[1].isdigit()):
            raise MyNoNumberError(f"{input_number} - не число. "
                                  f"Возможно присутствуют недопустимые/отсутствуют необходимые символы.")
    elif count_of_dots == 0:
        if not input_number.isdigit():
            raise MyNoNumberError(f"{input_number} - не число. "
                                  f"Возможно присутствуют недопустимые/отсутствуют необходимые символы.")
    else:
        raise MyNoNumberError(f"{input_number} - не число. В числе не может быть > 1 плавающей точки.")


print("Приветствую, пользователь!\nПрограмма фильтрует вещественные числа из строк без использования float() и int().")
print("Для вывода суммы чисел - наберите числа через пробел;\n"
      "Для выхода из программ - введи 'q'")
result = []
run = True
while run:
    input_numbers = input("Введите числа через пробел: \n").split()
    for number in input_numbers:
        if number == "q" or number == "'q'" or number == "Q":
            print("Завершение работы...")
            run = False
            break
        else:
            try:
                check_non_positive_number(number.split("-")[1]) if number.startswith("-") and number.count("-") == 1 \
                    else check_non_positive_number(number)
                result.append(number)
            except MyNoNumberError as err:
                print(err)

print(f"Конечный список: {result}")
