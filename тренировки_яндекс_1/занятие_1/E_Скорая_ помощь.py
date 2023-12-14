"""
Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению, когда диспетчер
получил вызов, он успел записать только адрес дома и номер квартиры K1, а затем связь прервалась.
Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала в
квартиру K2, которая расположена в подъезда P2 на этаже N2. Известно, что в доме M этажей и
количество квартир на каждой лестничной площадке одинаково. Напишите программу, которая вычилсяет
номер подъезда P1 и номер этажа N1 квартиры K1.
"""

import math


def count_on_floor(k2, n2, p2, m):
    return math.ceil(k2 / (n2 + (p2 - 1) * m))


def solution(k1, k2, n2, p2, m):
    res = []
    c = count_on_floor(k2, n2, p2, m)
    p1 = math.ceil(k1 / (c * m))
    n1 = math.ceil((k1 / c) - ((p1 - 1) * m))
    p = p1
    if k2 <= 10:
        p = 0
    if p2 == p1:
        p = -1
        n1 = -1
    res = [p, n1]
    return res


K1, M, K2, P2, N2 = map(int, input().split())

print(*solution(K1, K2, N2, P2, M))
