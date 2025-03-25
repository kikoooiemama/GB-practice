# Created by Nikolay Pakhomov 19.07.2024
# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.


s = 'papa'


def search_strings(s):
    n = len(s)
    arr_str = set()
    for i in range(1, n):

        for j in range(n - i + 1):

            k = hash(s[j:j + i])

            if k not in arr_str:
                arr_str.add(k)

    return len(arr_str)


print(f'Количество подстрок: {search_strings(s)}')
