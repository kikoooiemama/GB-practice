# Created by Nikolay Pakhomov 19.07.2024
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', "name, profit_list, avg_profit")

lst = []
for i in range(int(input('Введите количество компаний: '))):
    arg = input('Введите в строку имя и поквартальную прибыль через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:4]))))

avg = mean([i.avg_profit for i in lst])
print('_' * 70)
print(f"Средняя прибыль всех компаний за год: {avg}")
print('_' * 70)
for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg_profit}')

print('_' * 70, '\n')

print('Компании с прибылью меньше средней:')
for i in lst:
    if i.avg_profit < avg:
        print(i.name)

print('Компании с прибылью больше средней:')
for i in lst:
    if i.avg_profit > avg:
        print(i.name)
