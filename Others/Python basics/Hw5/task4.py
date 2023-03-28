# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# Как я понял из за задания. Английские числительные это One, Two, Three, Four. Им соответственно сопоставляются русские
# числительные Один, Два и т.д

source = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

try:
    input_file = open("text_4.txt", "r", encoding="utf-8")
    output_file = open("text_4_output.txt", "w", encoding="utf-8")
    output_file.writelines([line.replace(line.split()[0], source.get(line.split()[0])) for line in input_file])
    input_file.close()
    output_file.close()
except IOError as err:
    print("IOError: Ошибка при открытии/чтении/записи файла\n", err)

