# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за
# получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def fact(num):
    result = 1
    for i in range(num + 1):
        yield [i, result]
        result *= i + 1


print("Приветствую, пользователь!")
try:
    n = int(input("Введите значение 'n': \n"))
    if n < 0:
        raise ValueError
    for el in fact(n):
        print(f"{el[0]}! = {el[1]}")
except ValueError:
    print("Ошибка! Некорректное входное значение!")
