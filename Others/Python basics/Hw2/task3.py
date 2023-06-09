# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и dict.

print("Приветствую, пользователь!")
source_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето",
               "Осень", "Осень", "Осень", "Зима"]
source_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
               9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
mode = bool(input("Для Dict оставьте поле пустым, для List введите что-нибудь: "))
# True - use List, False - use dict
while True:
    input_number = input("\nВведите месяц числом от 1 до 12: ")
    # проверка на число в строке
    if input_number.isdigit():
        input_number = int(input_number)
        # проверка в каком интервале число
        if 0 < input_number < 13:
            if mode:
                print(f"\nВремя года: {source_list[input_number - 1]}")
            else:
                print(f"\nВремя года: {source_dict.get(input_number)}")
            break
        else:
            print("Ошибка! Введенное число не попадает в интервал [1, 12]")
    else:
        print("Ошибка при вводе месяца!")
