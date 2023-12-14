"""
Возвращает n элемент последовательности Фибоначи.
"""


def ith_fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        # print(current)
    return current


print(ith_fibonacci(10))
