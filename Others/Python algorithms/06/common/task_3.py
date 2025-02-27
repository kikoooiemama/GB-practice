# Created by Nikolay Pakhomov 13.02.2025
# Как работает list
lst = []

lst.append(1)
lst.extend([2, 3, 4])

print(lst)

# При создании пустого списка, Python зарезервировал 4 ячейки размером 8 байт (64 битная ОС).

lst.insert(1, 5)
print(lst)

# Для расширения Python сделал allocated: 8, выделил еще 4 ячейки, увеличив размер списка до 8. Почему так?

allocated = 0
for newsize in range(100):
    if allocated < newsize:
        # формула гвиде ван росса.
        new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)

        allocated = newsize + new_allocated

    print(newsize, allocated)

# После резервирования новых ячеек -> Python начинает двигать адреса и добавляет пятерку в ячейку 1.

last = lst.pop()
print(lst, last)

# size = 4, allocated = 8. Ячейка все еще ссылается на 4, но сам список уже не учитывает.

last = lst.pop()
print(lst, last)

# size = 3, allocated = 6. Python каждый раз делает проверку и уменьшает объем выделенной памяти.

lst.remove(5)
print(lst, last)

# Python переписал адреса, лист уменьшил размер, а также произошло уменьшение выделенной памяти. Ячейка 2 теперь стала
# свободной.
