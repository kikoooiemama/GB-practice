# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

run = True
print("Приветствую, пользователь! Это программа по вычислению простых действий с 2-мя числами" +
      "\nВозможные действия: " +
      "\nсложение - '+'" +
      "\nвычитание - '-'" +
      "\nумножение - '*'" +
      "\nделение - '/'" +
      "\nвозведение в степень - '**'" +
      "\n")
print("Для выхода введите 'q'")
while run:
    operation = input("\nВведите действие: '+', '-', '*', '/', '**' или 'q'\n")
    if operation == "+" or operation == "'+'":
        a = float(input("Введите первое слагаемое: "))
        b = float(input("Введите второе слагаемое: "))
        answer = a + b
        print("\nРезультат: {}".format(answer))
    elif operation == "-" or operation == "'-'":
        a = float(input("Введите уменьшаемое: "))
        b = float(input("Введите вычитаемое: "))
        answer = a - b
        print("\nРезультат: {}".format(answer))
    elif operation == "*" or operation == "'*'":
        a = float(input("Введите первый множитель: "))
        b = float(input("Введите второй множитель: "))
        answer = a * b
        print("\nРезультат: {}".format(answer))
    elif operation == "/" or operation == "'/'":
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        answer = a / b
        print("\nРезультат: {}".format(answer))
    elif operation == "**" or operation == "'**'":
        a = float(input("Введите основание: "))
        b = float(input("Введите значение степени: "))
        answer = a ** b
        print("\nРезультат: {}".format(answer))
    elif operation == "q" or operation == "'q'":
        print("Выход из программы")
        run = False
    else:
        print("Введенное действие не соответствует возможностям программы." +
              "\nПопробуйте еще раз :)")
