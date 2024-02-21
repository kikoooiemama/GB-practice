# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков. Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.


# a. Сортировка массива чисел по возрастанию.
# b.
# Алгоритм №1.
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


# Алгоритм №2.
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


# Алгоритм №3.
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

# c, d, e.
# Алгоритм №1
# 1000 loops, best of 5: 14.1 usec per loop - 10 elements
# 1000 loops, best of 5: 811 usec per loop - 100 elements
# 1000 loops, best of 5: 89.9 msec per loop - 1000 elements

# Алгоритм №2
# 1000 loops, best of 5: 10.4 usec per loop - 10 elements
# 1000 loops, best of 5: 341 usec per loop - 100 elements
# 1000 loops, best of 5: 31.8 msec per loop - 1000 elements

# Алгоритм №3
# 1000 loops, best of 5: 13.8 usec per loop - 10 elements
# 1000 loops, best of 5: 162 usec per loop - 100 elements
# 1000 loops, best of 5: 2.06 msec per loop - 1000 elements


# Вывод
# Сложность алгоритма №1: O(n^2)
# Сложность алгоритма №2: O(n^2)
# Сложность алгоритма №3: O(n log n)
# Самым лучшим оказался алгоритм №3. Он самый быстрый.
