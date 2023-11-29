"""
4. С помощью рекурсии напишите функцию, которая принимает строку и возвращает первый попавшийся
индекс, соответствующий символу "х". Например, строка "abcdefghijklmnopqrstuvwxyz" содержит "х"
в позиции с индексом 23. Чтобы было проще, допустим, что в передаваемой функции строке есть как
минимум один символ "х".
"""


def find_x(string, index=0):

    if string[0] == "x":
        return index
    else:
        return find_x(string[1:], index + 1)


print(find_x("abcdefghijklmnopqrstuvwxyz"))
print(find_x("x"))
