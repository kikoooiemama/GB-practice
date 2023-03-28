# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1   ООО   10000   5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).

import json

result = []
try:
    with open("text_7.txt", "r", encoding="utf-8") as dataset:
        companies_profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in dataset}
        average_profit = {
            "average_profit": sum([int(profit) for profit in companies_profit.values() if profit >= 0]) / len(
                [int(profit) for profit in companies_profit.values() if profit >= 0])}
        result.append(companies_profit)
        result.append(average_profit)
    with open("text_7_output.json", "w", encoding="utf-8") as output_file:
        # "\u0421\u043a\u0430\u0437\u043a\u0430" - чтобы этого не было: ensure_ascii = False
        # для отступов вбиваем параметр indent
        json.dump(result, output_file, indent=4, ensure_ascii=False)
except IOError as err:
    print("IOError: Ошибка при открытии/чтении/записи файла\n", err)
except ValueError as err:
    print("ValueError: Ошибка конвертации str в int\n", err)
