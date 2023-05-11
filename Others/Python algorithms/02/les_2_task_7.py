# Created by Nikolay Pakhomov 10.05.2023

# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def check_eq(n):
    right = n * (n + 1) / 2
    left = 0.0
    for i in range(1, n + 1):
        left += i
    if left == right:
        return f"Равенство выполняется: {left}={right}"
    else:
        return f"Равенство не выполняется: {left}!={right}"


print(check_eq(12353432))
