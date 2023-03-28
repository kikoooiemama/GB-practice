# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print("Приветствую, пользователь!" +
      "\nПрограмма находит наибольшую цифру во всем числе.\n")
number = int(input("Введите целое число: \n"))
if number < 0:
    number = -number
maximum = 0
while number > 0:
    unit = number % 10
    number = number // 10
    if maximum < unit:
        maximum = unit
print(f"Самая большая цифра: {maximum}")
