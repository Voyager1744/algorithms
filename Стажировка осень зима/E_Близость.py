"""
Определим близость двух целочисленных массивов как длину их наибольшего совпадающего префикса
Примеры:

Близость [1, 2, 1, 3] и [1, 2, 3, 2] равна
2
 — префикс [1, 2] совпадает;
Близость [1, 2, 3] и [3, 2, 1] равна
0
.
Дано
n
 целочисленных массивов

Необходимо вычислить сумму близостей массивов

 для каждой пары

Формат ввода
Первая строка содержит одно целое число
n

  — количество массивов.
Каждый массив задаётся двумя строками.
Первая строка описания массива содержит единственное целое число
k

  — размер
i
-го массива.
Вторая строка описания содержит
ki
 целых чисел
\
 — элементы
i
-го массива.
"""


def get_prefix_sum(arr):
    prefix_sum = [0]
    current_sum = 0

    for num in arr:
        current_sum += num
        prefix_sum.append(current_sum)

    return prefix_sum


def get_proximity_optimized(prefix_sum_a, prefix_sum_b):
    min_len = min(len(prefix_sum_a), len(prefix_sum_b))
    last_common_prefix = 0

    for k in range(min_len):
        if prefix_sum_a[k] == prefix_sum_b[k]:
            last_common_prefix = k
        else:
            break

    return last_common_prefix


n = int(input())
arrays = []

for _ in range(n):
    len_arr = int(input())
    arr = list(map(int, input().split()))
    prefix_sum = get_prefix_sum(arr)
    arrays.append(prefix_sum)

res = 0

for i in range(n):
    for j in range(i + 1, n):
        proximity = get_proximity_optimized(arrays[i], arrays[j])
        res += proximity

print(res)

# Частичное решение. TL на 37 тесте
