"""
Сравните два числа в двоичной системе счисления.
Числа представлены последовательностью слов без пробелов, обозначающих цифры (0 — zero, 1 — one).
"""

S1 = int(input().replace("zero", "0").replace("one", "1"), 2)
S2 = int(input().replace("zero", "0").replace("one", "1"), 2)

if S1 > S2:
    print(">")
elif S1 < S2:
    print("<")
else:
    print("=")

