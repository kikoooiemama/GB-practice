# Created by Nikolay Pakhomov 10.05.2023

# Алгоритм Евклида. Поиск НОД.

# Долго (вычитание долгое)
def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


# Тратиться дополнительная память на сохранение информации о рекурсивном вызове функции + риск получить ошибку
# переполнения стека вызова функции
def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(gcd(540, 24458732646))
print(gcd2(540, 24458732646))
print(gcd3(540, 24458732646))
