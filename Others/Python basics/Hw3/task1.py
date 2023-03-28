# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    """Функция деления двух рациональных чисел.

    :param dividend: Делимое (float)
    :param divider: Делитель (float)
    :return: Результат деления (float)
    """
    try:
        dividend = float(dividend)
        divider = float(divider)
        answer = dividend / divider
        return round(answer, 5)
    except ZeroDivisionError:
        return "Ошибка! Делитель не может быть равен 0!"
    except ValueError:
        return "Введены некорректные числа!"


print("Приветствую, пользователь!")
result = division(input("Введите делимое: \n"), input("Введите делитель: \n"))
print(f"Результат: {result}")
