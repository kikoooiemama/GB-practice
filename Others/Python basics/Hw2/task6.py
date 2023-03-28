# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть
# характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.

# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например,
# название. Тогда значение — список значений-характеристик, например, список названий товаров.

print("Приветствую, пользователь!")
print("Реализуем структуру данных 'Товары'\n")
run = True
current_catalog = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."})
]
print("Текущий каталог товаров: ")
for item in current_catalog:
    print(item)
commands = ("q", "add", "get", "show")
print(f"\nДля работы используйте следующие команды меню:"
      f"\n{commands[0]:<8} - выход"
      f"\n{commands[1]:<8} - добавить/перезаписать характеристику товару"
      f"\n{commands[2]:<8} - вывести аналитику"
      f"\n{commands[3]:<8} - показать текущий каталог товаров")
while run:
    command = input("\nВведите команду: ")
    # quit
    if command == "q" or command == "'q'":
        run = False
    # add feature to good
    elif command == "add" or command == "'add'":
        number = input("Введите номер товара: ")
        feature = input("Введите характеристику товара: ").strip()
        value = input("Введите значение характеристики: ").strip()
        try:
            number = int(number)
            create_good = True
            # check good num in catalog
            for good in current_catalog:
                if good[0] == number:
                    # features dict
                    good[1][feature] = value
                    create_good = False
                    break
            if create_good:
                current_catalog.append((number, {feature: value}))
        except ValueError:
            print("Ошибка при вводе номера товара!")
    # create analytic
    elif command == "get" or command == "'get'":
        analytic = {}
        # add keys with empty list
        for good in current_catalog:
            for key in good[1].keys():
                analytic[key] = []
        # add lists
        for good in current_catalog:
            for key, value in good[1].items():
                analytic.get(key).append(value)
        print("\nАналитика о товарах:")
        for k, v in analytic.items():
            analytic.update({k: list(set(v))})
            print(f"{k:<16}: {v}")
    # show catalog
    elif command == "show" or command == "'show'":
        for item in current_catalog:
            print(item)
    # other cases
    else:
        print("Неизвестная команда. Попробуйте еще!")
