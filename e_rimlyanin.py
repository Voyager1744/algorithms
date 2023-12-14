"""
Вам дано число, записанное римскими цифрами. Получите это же число в обычной записи (арабскими цифрами).
Римская запись чисел может включать следующие символы:

’I’ — 1
’V’ — 5
’X’ — 10
’L’ — 50
’C’ — 100
’D’ — 500
’M’ — 1000
Цифры ’I’, ’X’, ’C’ и ’M’ нельзя использовать более трех раз подряд. Цифры ’V’,
’L’ и ’D’ нельзя использовать более одного раза во всей записи числа.
Обыкновенно цифры записывают по убыванию слева направо. Например, число 350
будет записано как ’CCCL’.
Однако есть исключения:

Чтобы получить ’4’ или ’9’, надо поставить ’I’ перед ’V’ или ’X’ соответственно
Чтобы получить ’40’ или ’90’, надо поставить ’X’ перед ’L’ или ’C’.
Чтобы получить ’400’ или ’900’, надо поставить ’C’ перед ’D’ или ’M’.

"""


def convert_to_arabic(s: str) -> int:
    chars = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    n = len(s)
    if n == 0:
        return -1
    count_v, count_l, count_d = 0, 0, 0

    for char in s:
        if char == "V":
            count_v += 1
        if char == "L":
            count_l += 1
        if char == "D":
            count_d += 1
        if char not in chars.keys():
            return -1
    if count_v > 1 or count_l > 1 or count_d > 1:
        return -1
    if "IIII" in s or "XXXX" in s or "CCCC" in s or "MMMM" in s:
        return -1

    result = chars.get(s[0], 0)
    for i in range(1, n):
        current = chars.get(s[i], 0)
        prev = chars.get(s[i - 1], 0)
        if current == 0:
            return -1
        if prev >= current:
            result += current
        else:
            if prev * 5 == current or prev * 10 == current:
                result -= prev
                result += current - prev
                if i > 1:
                    prev_prev = chars.get(s[i - 2], 0)
                    if prev_prev == prev:
                        return -1
            else:
                return -1
    return result


roman_number = input()
print(convert_to_arabic(roman_number))
