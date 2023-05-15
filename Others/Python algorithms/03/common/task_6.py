# Created by Nikolay Pakhomov 15.05.2023


# Задача. Пользователь вводите количество предприятий, названия, плановую и фактическую прибыль каждого предприятия.
# Вычислить процент выполнения плана и вывести данные с предварительной фильтрацией.

k = int(input("Введите количество предприятий: "))
enterprises = {}

for i in range(1, k + 1):
    name = input("Введите название предприятия: ")
    enterprises[name] = [float(input("План:")), float(input('Факт: '))]
    # процент выполнения плана
    enterprises[name].append(enterprises[name][1] / enterprises[name][0])

# условие фильтрации предприятий
print("Фактическая прибыль больше 10, но план не выполнен (меньше 100%)")
for key, value in enterprises.items():
    if value[1] > 10 and value[2] < 1:
        print(f'Предприятие {key} заработало {value[1]}, что составило {value[2] * 100:.2f}%')
