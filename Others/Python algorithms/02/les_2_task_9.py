# Created by Nikolay Pakhomov 10.05.2023

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

print("Вводите по очереди натуральные числа. Для прекращения ввода введите '0'.")
m = 0
m_sum = 0
while True:
    c = int(input("Ввод натурального число: "))
    if c == 0:
        break
    c_sum = 0
    # подсчет суммы цифр без использования массивов
    b = c
    while b > 0:
        c_sum += b % 10
        b //= 10
    # проверка наибольшей суммы цифр
    if c_sum > m_sum:
        m = c
        m_sum = c_sum
print(f"Натуральное число с наибольшей суммой цифр: {m}")
print(f"Сумма цифр: {m_sum}")
