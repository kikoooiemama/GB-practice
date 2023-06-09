# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
# чисел будет добавляться к уже подсчитанной сумме.

# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

def summation_of_numbers():
    """Функция считывает сумму всех введенных через пробел чисел до тех пор пока не будет введен специальный символ 'q'.

    ввод чисел -- строго через пробел вводятся любые действительные числа;
    'q' -- специальный символ. При вводе этого символа программа завершает работу;
    :return: Сумма всех введеных пользователем чисел до ввода специального символа 'q'.
    """
    result = 0
    while True:
        input_numbers = input("Введите числа через пробел: \n").split()
        for number in input_numbers:
            if number == "q" or number == "'q'" or number == "Q":
                print("Завершение работы...")
                return result
            else:
                try:
                    result += float(number)
                except ValueError:
                    continue
        print(f"Промежуточная сумма: {result}")


print("Приветствую, пользователь!")
print("Для вывода суммы чисел - набери числа через пробел;\n"
      "Для выхода из программ - введи 'q'")
print(f"Конечный результат: {summation_of_numbers()}")
# example of str: 12 sf 4 6g -42 dfg 3.333
