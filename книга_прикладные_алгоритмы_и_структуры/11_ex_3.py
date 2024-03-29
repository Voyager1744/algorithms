"""
3. Есть последовательность так называемых треугольных чисел, которая начинается
  как 1, 3, 6, 10, 15, 21 и продолжается с N-го числа в шаблоне, равного N плюс
  предыдущее число. Например, седьмое число последовательности - 28, то есть 7
  (номер числа N) плюс 21 (предыдущее число последовательности).
  Напишите функцию, которая принимает номер числа N и возвращает соответствующее число
  последовательности. Например, при передаче этой функции значения 7 она должна вернуть 28.
"""


def triangle_number(n):
    if n == 1:
        return 1
    else:
        return n + triangle_number(n - 1)


print(triangle_number(7))
