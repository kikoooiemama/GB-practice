# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
# нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.

print("Приветствую, пользователь!")
rating = [7, 5, 3, 3, 2]
run = True
print(f"Рейтинг: {rating}")
print("Введите новый элемент рейтинга или введите 'q' для выхода из программы!")
while run:
    input_number = input("Ввод: ")
    if input_number == "q" or input_number == "'q'":
        run = False
    else:
        try:
            input_number = int(input_number)
            index = 0
            # ищем index для input_number в невозрастающей последовательности чисел.
            for rating_number in rating:
                if input_number <= rating_number:
                    index += 1
            # установка по индексу
            rating.insert(index, input_number)
            print(f"Рейтинг с учетом нового элемента: {rating}")
        except ValueError:
            print("Ошибка! Недопустимое значение рейтинга!")
