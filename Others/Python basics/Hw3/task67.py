# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func():
    """Функция вырезает из введенных пользователем слов слова, написанные маленькими латинскими буквами, и у каждого
    такого слова переводит первую букву из нижнего регистра в верхний.

    :return: Список слов, начинающихся с заглавной буквы (list).
    """
    words = input("Введите слова из маленьких латинских букв через пробел: \n").split()
    result = []
    for word in words:
        # The isalpha() method returns True if all the characters are alphabet letters (a-z).
        # ascii(word) -> 'nice\ -> [1:-1] -> nice
        if word.islower() and ascii(word)[1:-1].isalpha():
            result.append(word.title())
    return result


print("Приветствую, пользователь!")
for new_word in int_func():
    print(new_word, end=" ")
# example of str: nice авп вапgjh true hello jasроп 123skgjh world вавопkdjhgf cool
