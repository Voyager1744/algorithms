"""
Разработчики любят проводить свободное время за настольными играми. Иногда это шахматы,
иногда — UNO, а иногда — шашки. Однако, когда неопытные игроки садятся за шашки, они периодически
допускают ошибки (прямо как в программировании!) и не рубят шашку соперника, когда такая
возможность есть.

Чтобы избежать ошибок, разработчики решили написать программу, которая будет по текущей позиции
определять, можно ли сходить так, чтобы срубить шашку противника. Но прямо сейчас у них много
других важных проектов, поэтому запрограммировать анализатор позиции попросили вас.

Для тех, кто давненько не брал в руки шашек, напомним правила:

все шашки стоят на полях одного цвета;
одна шашка может срубить другую, если та стоит на соседней клетке по диагонали и при этом в
следующей диагональной клетке в направлении соперника нет никакой другой шашки.

"""


class Chip:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.S1 = self.x - 1, self.y - 1
        self.S2 = self.x - 1, self.y + 1
        self.S3 = self.x + 1, self.y - 1
        self.S4 = self.x + 1, self.y + 1

    def coordinates(self):
        return self.x, self.y

    def neighbours(self):
        return self.S1, self.S2, self.S3, self.S4

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return self.__str__()


def valid_coords(x, y, N, M):
    return 1 <= x <= N and 1 <= y <= M





def main():
    N, M = map(int, input().split())
    w = int(input())
    white_chips = []
    for _ in range(w):
        x, y = map(int, input().split())
        white_chips.append(Chip(x, y))
    b = int(input())
    black_chips = []
    for _ in range(b):
        x, y = map(int, input().split())
        black_chips.append(Chip(x, y))
    start_player = input()

    def check_neighbours(chips, chip):
        for nei in chip.neighbours():
            if Chip(*nei) in chips and valid_coords(nei[0], nei[1], N, M):
                if nei == chip.S1:
                    return 'S1'
                elif nei == chip.S2:
                    return 'S2'
                elif nei == chip.S3:
                    return 'S3'
                elif nei == chip.S4:
                    return 'S4'
        return False

    if start_player == 'white':
        start_list = white_chips
        second_list = black_chips
    else:
        start_list = black_chips
        second_list = white_chips

    for chip in start_list:
        S = check_neighbours(second_list, chip)
        if S:
            if S == 'S1':
                neibour = Chip(*chip.S1).S1
            elif S == 'S2':
                neibour = Chip(*chip.S2).S2
            elif S == 'S3':
                neibour = Chip(*chip.S3).S3
            elif S == 'S4':
                neibour = Chip(*chip.S4).S4

            if Chip(*neibour) not in second_list and Chip(*neibour) not in start_list and valid_coords(*neibour, N, M):
                print('Yes')
                return

    print("No")


main()

# b1 = Chip(1, 1)
# b2 = Chip(1, 1)
# b3 = Chip(1, 2)
#
# L = [b2, b3]
#
# print(b1 in L)
# print(b1.S4)
#
# neiChip = Chip(*b1.S4)
# print(neiChip.S4)
