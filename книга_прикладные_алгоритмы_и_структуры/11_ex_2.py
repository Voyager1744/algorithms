"""
2. С помощью рекурсии напишите функцию, которая принимает массив чисел и возвращает новый, в котором
будут только четные.
"""


def even_numbers(arr):
    if len(arr) == 0:
        return []
    if arr[0] % 2 == 0:
        return [arr[0]] + even_numbers(arr[1:])
    else:
        return even_numbers(arr[1:])


print(even_numbers([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]))
