# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных будет свидетельствовать пустая строка.

print("Приветствую, пользователь!")
f = open("text_1.txt", "w", encoding="utf-8")
data = "default"
# "" is False, other str is True
while data:
    data = input("Введите данные или нажмите Enter для выхода: \n")
    f.close() if data == "" else print(data, file=f)
