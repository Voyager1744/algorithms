"""
Два друга A и B
 постоянно играют в коллекционную карточную игру (ККИ), поэтому у каждого игрока скопилась довольно
 большая коллекция карт.
Каждая карта в данной игре задаётся целым числом (одинаковые карты — одинаковыми числами, разные
карты — разными).
Таким образом коллекцию можно представить как неупорядоченный набор целых чисел (с возможными
повторениями).
После каждого изменения коллекций друзья вычисляют показатель разнообразия следующим образом:

A
 и
B
 выкладывают на стол все карты из своей коллекции в два раздельных ряда;
Далее друзья итеративно делают следующее:
Если среди лежащих на столе карт игрока
A
 есть такая же карта, как и среди лежащих карт игрока
B
 — каждый игрок убирает данную карту со стола;
Если таковых совпадений нет — процесс заканчивается.
Разнообразием коллекций друзья называют суммарное количество оставшихся карт на столе.
Обратите внимание: друзья убирают карты только со стола, карты не удаляются из коллекций при
вычислении разнообразия.
Даны начальные состояния коллекций игроков, а также
Q
 изменений их коллекций. После каждого изменения необходимо вычислить разнообразие коллекций друзей.
"""


# def check_diversity(col_A: dict, col_B: dict) -> int:
#     res = {}
#     col_a = col_A.copy()
#     col_b = col_B.copy()
#     for key in col_a:
#         if key in col_b:
#             res[key] = col_a[key] - col_b[key]
#             col_b.pop(key)
#         else:
#             res[key] = col_a[key]
#     for key in col_b:
#         res[key] = col_b[key]
#
#     return sum(res.values())
#
#
# def change_collection(tipe: int, card: int, collection: dict) -> dict:
#     if tipe == 1:
#         if card in collection:
#             collection[card] += 1
#         else:
#             collection[card] = 1
#     elif tipe == -1:
#         collection[card] -= 1
#         if collection[card] == 0:
#             collection.pop(card)
#
#     return collection
#
#
# result = []
#
# N, M, Q = map(int, input().split())
#
# A = {}
# a_list = list(map(int, input().split()))
# for _ in range(N):
#     key = a_list.pop()
#     if key in A:
#         A[key] += 1
#     else:
#         A[key] = 1
#
# B = {}
# b_list = list(map(int, input().split()))
# for _ in range(M):
#     key = b_list.pop()
#     if key in B:
#         B[key] += 1
#     else:
#         B[key] = 1
#
# for _ in range(Q):
#     tipe, player, cord = input().split()
#     if player == "A":
#         A = change_collection(int(tipe), int(cord), A)
#     else:
#         B = change_collection(int(tipe), int(cord), B)
#
#     result.append(check_diversity(A, B))
#
# print(*result)

from collections import Counter


def check_diversity(col_A: dict, col_B: dict) -> int:
    common_keys = set(col_A.keys()) & set(col_B.keys())
    print(common_keys)
    res = {key: col_A[key] - col_B[key] for key in common_keys}
    res.update({key: col_A[key] for key in set(col_A.keys()) - common_keys})
    res.update({key: col_B[key] for key in set(col_B.keys()) - common_keys})
    return sum(res.values())


def change_collection(tipe: int, card: int, collection: dict) -> dict:
    collection[card] += tipe
    if collection[card] == 0:
        del collection[card]
    return collection


result = []

N, M, Q = map(int, input().split())

A = Counter(map(int, input().split()))
B = Counter(map(int, input().split()))

cumulative_A = Counter(A)
cumulative_B = Counter(B)

for _ in range(Q):
    tipe, player, cord = input().split()
    cord = int(cord)

    if player == "A":
        cumulative_A = change_collection(int(tipe), cord, cumulative_A)
    else:
        cumulative_B = change_collection(int(tipe), cord, cumulative_B)

    result.append(check_diversity(cumulative_A, cumulative_B))

print(*result)

# Частичное решение. TL на 14 тесте
