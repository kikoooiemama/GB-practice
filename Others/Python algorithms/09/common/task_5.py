# Created by Nikolay Pakhomov 25.03.2025
import hashlib


# 1. Сравнение строк с помощью хеширования
def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f"hash 1 = {ha}\nhash 2 = {hb}")

    return ha == hb


s_1 = input('Введите строку 1: ')
s_2 = input('Введите строку 2: ')

print('Строки одинаковые' if is_eq_str(s_1, s_2, True) else 'Строки разные')


# 2. Поиск подстроки в строке (Рабин, Карп)
def rabin_karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) >= len(subs), 'Подстрока длиннее строки'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if s[i:i + len_sub] == subs:
                return i

    return -1


s_1 = input('Введите строку: ')
s_2 = input('Введите подстроку для поиска: ')

pos = rabin_karp(s_1, s_2)
print(f"Подстрока найдена в позиции {pos}" if pos != -1 else "Подстрока не найдена")
