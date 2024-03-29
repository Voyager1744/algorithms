"""

2. Следующая функция использует рекурсию для определения N-го числа из последовательности Голомба.
Но это ужасно неэффективно! Оптимизируйте функцию с помощью мемоизации (чтобы выполнить это
упражнение, вам вовсе не обязательно понимать, как вычисляется эта последовательность).
"""


def golomb(n, memo=None):
    if memo is None:
        memo = {}
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]


print(golomb(10))
