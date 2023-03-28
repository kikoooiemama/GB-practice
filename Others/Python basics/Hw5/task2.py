# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

# как я понял text_2 должен быть создан мной, в архиве файликов не было text_2.txt
f = open("text_2.txt", "r", encoding="utf-8")
data = [line for line in f.readlines()]
print(f"Всего строк: {len(data)}")
result = ([f"{num}-ая строка: {len(value.split())} слов" for num, value in enumerate(data, 1)])
print(*result, sep="\n")
f.close()