# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

my_func = lambda number_1, number_2, number_3: sum([number_1, number_2, number_3]) - min(number_1, number_2, number_3)

print("Приветствую, пользователь!")
try:
    input_number_1 = float(input("Введите 1 число: \n"))
    input_number_2 = float(input("Введите 2 число: \n"))
    input_number_3 = float(input("Введите 3 число: \n"))
    print(f"Результат: {round(my_func(input_number_1, input_number_2, input_number_3), 5)}")
except ValueError:
    print("Введено некорректное число!")
