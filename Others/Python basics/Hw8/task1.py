# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, input_date):
        self.date = input_date

    @classmethod
    def convert(cls, input_date):
        try:
            numbers = list(map(int, str(input_date).split("-")))
            if len(numbers) != 3:
                raise ValueError("Должно быть 3 числа. День, месяц и год.")
            numbers = cls.validate(numbers)
        except ValueError as err:
            return cls(f"Неккоректные входные данные.\n{err}")
        else:
            return cls(numbers)

    # входные данные: список в виде чисел день, месяц, год
    @staticmethod
    def validate(input_date):
        source_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                       9: 30, 10: 31, 11: 30, 12: 31}
        if len(input_date) != 3:
            raise ValueError("Во входных данных должно быть 3 числа: день, месяц и год.")
        for number in input_date:
            if type(number) is not int:
                raise ValueError(
                    f"Нечисловые параметры. День: {input_date[0]}, Месяц: {input_date[1]}, Год: {input_date[2]}.")
        year = input_date[2]
        if year < 0:
            raise ValueError(f"Отрицательный год: {input_date[2]}")
        month = input_date[1]
        if list(source_dict.keys()).count(month) == 0:
            raise ValueError(f"Несуществующий месяц: {input_date[1]}")
        day = input_date[0]
        if month == 2:
            if year % 4 == 0 and (day < 1 or day > source_dict.get(month)):
                raise ValueError(
                    f"Несуществующий день: {input_date[0]} в месяце {input_date[1]} в високосном {input_date[2]} году.")
            elif year % 4 != 0 and (day < 1 or day >= source_dict.get(month)):
                raise ValueError(
                    f"Несуществующий день: {input_date[0]} в месяце {input_date[1]} в невисокосном {input_date[2]} году.")
        else:
            if day < 1 or day > source_dict.get(month):
                raise ValueError(f"Несуществующий день: {input_date[0]} в месяце {input_date[1]}.")
        print("Валидация прошла успешно!")
        return {"День": day, "Месяц": month, "Год": year}


date_str = "29-02-2020"
date = Date.convert(date_str)
print(date.date)
