"""
Решите в целых числах уравнение:

,

a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых числах нет.

"""


def solution(a, b, c):
    if a == 0:
        if b >= 0 and b == c**2:
            return "MANY SOLUTIONS"
        return "NO SOLUTION"
    if c < 0:
        return "NO SOLUTION"
    x = (c**2 - b) / a

    if (a * x + b) < 0:
        return "NO SOLUTION"

    if x != int(x):
        return "NO SOLUTION"

    return int(x)


a = int(input())
b = int(input())
c = int(input())

print(solution(a, b, c))
