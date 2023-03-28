# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

print("Приветствую, пользователь!")
input_data = input("Введите элементы списка, разделяя каждый элемент пробелом: \n")
input_data = input_data.split()
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Введенный список элементов: {input_data}")
# new_data = data.copy()
new_data = []
new_data.extend(input_data)
even = len(input_data)
odd = len(input_data) - 1
i = even if len(input_data) % 2 == 0 else odd
new_data[:i:2] = input_data[1:i:2]
new_data[1:i:2] = input_data[:i:2]
print(f"Результат: {new_data}")
