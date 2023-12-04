"""
3. Напишите три разные реализации функции, которая находит наибольшее число в массиве.
При этом сложность одной должна быть О(No), второй - O(Nlog N), а третьей - O(N).
"""


def max_number(numbers):
    numbers.sort()
    return numbers[-1]


def max_number2(numbers):
    """ Пример квадратичной сложности."""

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers[-1]


def max_number3(numbers):
    """ Пример линейной сложности."""

    greatest = numbers[0]
    for i in numbers:
        if i > greatest:
            greatest = i
    return greatest


print(max_number([1, 2, 3, 4, 5, 6]))
print(max_number2([1, 2, 3, 4, 5, 6]))
print(max_number3([1, 2, 3, 4, 5, 6]))
