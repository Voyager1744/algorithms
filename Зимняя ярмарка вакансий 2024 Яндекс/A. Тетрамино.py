"""На шахматном поле
8×8
 некоторые клетки пустые, а некоторые заняты фигурами.
Определите количество способов разместить тетрамино на этом поле, чтобы фигура занимала целиком
 четыре свободные клетки.
В задаче мы рассматриваем тетрамино только одного типа.

Формат ввода
Входные данные состоят из 8 строк по 8 символов. Пустая клетка задается точкой (‘.’),
а занятая звездочкой (‘*’).

Формат вывода
Выведите количество способов разместить тетрамино на поле.
"""


# Функция для проверки, можно ли разместить тетрамино в данном месте на доске
def can_place_tetromino1(board, row, col):
    if row + 1 >= len(board) or col - 1 < 0 or col + 1 >= len(board[0]):
        return False
    return (
        board[row][col] == "."
        and board[row + 1][col] == "."
        and board[row][col - 1] == "."
        and board[row][col + 1] == "."
    )


def can_place_tetromino2(board, row, col):
    if row - 1 < 0 or row + 1 >= len(board) or col + 1 >= len(board[0]):
        return False
    return (
        board[row][col] == "."
        and board[row - 1][col] == "."
        and board[row][col + 1] == "."
        and board[row + 1][col] == "."
    )


def can_place_tetromino3(board, row, col):
    if row - 1 < 0 or col - 1 < 0 or col + 1 >= len(board[0]):
        return False
    return (
        board[row][col] == "."
        and board[row - 1][col] == "."
        and board[row][col - 1] == "."
        and board[row][col + 1] == "."
    )


def can_place_tetromino4(board, row, col):
    if row - 1 < 0 or row + 1 >= len(board) or col - 1 < 0:
        return False
    return (
        board[row][col] == "."
        and board[row - 1][col] == "."
        and board[row][col - 1] == "."
        and board[row + 1][col] == "."
    )


def count_tetromino_placements(board):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if can_place_tetromino1(board, row, col):
                count += 1
            if can_place_tetromino2(board, row, col):
                count += 1
            if can_place_tetromino3(board, row, col):
                count += 1
            if can_place_tetromino4(board, row, col):
                count += 1
    return count


board = []
for _ in range(8):
    row = input().strip()
    board.append(row)

print(count_tetromino_placements(board))
