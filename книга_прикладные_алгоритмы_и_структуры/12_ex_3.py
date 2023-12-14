"""
3. Это реализация задачи, связанной с поиском «уникальных путей~, из прошлой главы.
Используйте мемоизацию для повышения ее эффективности:
def unique_paths(rows, columns)
return 1 if rows == 1 11 columns == 1
return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
end
"""


def find_path(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return find_path(rows - 1, cols) + find_path(rows, cols - 1)


print(find_path(3, 7))

"""
 Чтобы применить мемоизацию здесь, превратим количество строк и столбцоввключ,
 который может быть в форме простого массива[rows, columns]:
def unique_paths(rows, columns, memo={}) return 1 if rows == 1 11 columns == 1
    if !memo[[rows, columns]]
        memo[[rows, columns]] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
    end
    return memo[[rows, columns]] 
end
"""


def unique_paths(rows, cols, memo=None):
    if memo is None:
        memo = {}
    if rows == 1 or cols == 1:
        return 1
    if (rows, cols) in memo:
        return memo[(rows, cols)]
    memo[(rows, cols)] = unique_paths(rows - 1, cols, memo) + unique_paths(
        rows, cols - 1, memo
    )
    return memo[(rows, cols)]


print(unique_paths(3, 7))
