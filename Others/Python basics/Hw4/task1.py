# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём
# формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv


def calculate_salary():
    try:
        # hours, rate, bonus_payment = argv[1:]
        # salary = float(hours) * float(rate) + float(bonus_payment)
        hours, rate, bonus_payment = map(float, argv[1:])
        # if rate < 0:
        #     print("Разве ставка по оплате труда может быть отрицательной? :)")
        #     return
        salary = hours * rate + bonus_payment
        print(f"Заработная плата сотрудника: {salary}")
    except ValueError:
        print("Ошибка! Либо не удалось конвертировать в число, либо введено недостаточно значений!")


print("Приветствую, пользователь!")
calculate_salary()
