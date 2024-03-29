"""

5. Эта проблема известна как проблема «уникальных путей~: допустим, у вас есть сетка строк и
столбцов. Напишите функцию, которая принимает число строк и столбцов и вычисляет количество
возможных «кратчайших~ путей от верхнего левого квадрата до нижнего правого.

Например, так выглядит сетка с тремя строками и семью столбцами. Нам нужно перейти из
квадрата «S>.> (Старт) в квадрат «F>-> (Финиш)

Под «кратчайшим>-> путем подразумевается то, что каждый раз вы передвигаетесь на один шаг вправо:

или на один шаг вниз:

Ваша функция должна вычислять количество кратчайших путей.
"""


def find_path(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return find_path(rows - 1, cols) + find_path(rows, cols - 1)


print(find_path(3, 7))
