# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
# подсчёт средней величины дохода сотрудников.

try:
    dataset = open("text_3.txt", mode="r", encoding="utf-8")
    # print(f"{[line for line in dataset]}")
    # test = {line.split()[0]: line[:-1].split()[1] for line in dataset}
    datadict = {line.split()[0]: float(line.split()[1]) for line in dataset}
    print(f"Средняя величина дохода сотрудников: {round(sum(datadict.values()) / len(datadict), 2)}\n"
          f"Список сотрудников с окладом < 20 тысяч: ")
    employers_list = [item[0] for item in datadict.items() if item[1] < 20000]
    print(*employers_list, sep="\n")
    dataset.close()
except ValueError as err:
    print("ValueError: Ошибка при чтении доходов из БД\n", err)
except IOError as err:
    print("IOError: Ошибка при открытии или чтении файла\n", err)
