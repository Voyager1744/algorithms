""""""
"""В самолете n рядов и по три кресла слева и справа в каждом ряду. Крайние
кресла (A и F) находятся у окна, центральные (C и D) – у прохода. На
регистрацию приходят группы из одного, двух или трех пассажиров. Они желают
сидеть рядом, то есть на одном ряду и на одной стороне: левой или правой.
Например, группа из двух пассажиров может сесть на кресла B и C, но не
может сесть на кресла C и D, потому что они разделены проходом,
а также не может сесть на кресла A и C, потому что тогда они окажутся не 
рядом. Кроме того, один из пассажиров каждой группы очень требовательный –
он хочет сесть либо у окна, либо у прохода. Конечно же, каждая группа из 
пассажиров хочет занять места в ряду с как можно меньшим номером, ведь 
тогда они скорее выйдут из самолета после посадки. Для каждой группы 
пассажиров определите, есть ли места в самолете, подходящие для них.
Формат ввода
Первая строка содержит число n (1≤n≤100) – количество рядов в самолете. Далее в 
n строках вводится изначальная рассадка в самолете по рядам (от первого до 
n-го), где символами . (точка) обозначены свободные места, символами # (решетка) 
обозначены занятые места, а символами _ (нижнее подчеркивание) обозначен проход 
между креслами C и D каждого ряда.
Следующая строка содержит число 
m (1≤m≤100) – количество групп пассажиров. Далее в 
m строках содержатся описания групп пассажиров. Формат описания такой: 
numsideposition, где num – количество пассажиров (число 
1,2 или 3) side – желаемая сторона самолета (строка left или right), 
position – желаемое место требовательного пассажира (строка aisle или window).

Формат вывода
Если группа может сесть на места, удовлетворяющие ее требованиям, то выведите 
строку Passengers can take seats: и список их мест в формате 
rowletter, упорядоченный по возрастанию буквы места. Затем выведите в 
n строках получившуюся рассадку в самолете, в формате, описанном выше, причем 
места, занятые текущей группой пассажиров, должны быть обозначены символом X.
Если группа не может найти места, удовлетворяющие ее требованиям, то выведите 
строку Cannot fulfill passengers requirements.
Ответ сравнивается с правильным посимвольно, поэтому ваше решение не должно 
выводить никаких лишних символов, в том числе лишних переводов строк или 
пробельных символов в концах строк. В конце каждой строки (включая последнюю) 
должен быть выведен символ перевода строки.

"""


# n = int(input())
# RAWS = []
# for _ in range(n):
#     RAWS.append(input())
#
# m = int(input())
# GROUPS = []
# for _ in range(m):
#     GROUPS.append(input().split())


def find_seats(seating, num_passengers, side, position):
    for row in seating:
        # Check if the desired side has enough consecutive seats
        if side == "left":
            seats = row[:3]
        else:
            seats = row[4:]
        if seats.count(".") >= num_passengers:
            # Check if the desired position is available
            if position == "window" and seats[0] == ".":
                return seats[:num_passengers]
            elif position == "aisle" and seats[-1] == ".":
                return seats[-num_passengers:]
    return None


n = int(input())
seating = []
for _ in range(n):
    seating.append(input())

m = int(input())
for _ in range(m):
    num_passengers, side, position = input().split()
    num_passengers = int(num_passengers)

    seats = find_seats(seating, num_passengers, side, position)
    if seats is not None:
        row_letters = seating.index("".join(seats)) + 1
        print("Passengers can take seats:", end=" ")
        print("".join(seats), end="\n")

        for i in range(num_passengers):
            if side == "left":
                seating[row_letters - 1] = seating[row_letters - 1].replace(".", "X", 1)
            else:
                seating[row_letters - 1] = (
                    seating[row_letters - 1].rsplit(".", 1)[0] + "X"
                )

    else:
        print("Cannot fulfill passengers requirements.")

for row in seating:
    print(row)

    #
    #     res = []
    #     pas = '.' * int(group[0])
    #     count_pass = int(group[0])
    #     if group[1] == 'left':
    #         lit = ['A', 'B', 'C']
    #         pas = dict(zip(lit[:count_pass], list('.' * count_pass)))
    #
    #     elif group[1] == 'right':
    #         lit = ['D', 'E', 'F']
    #         pas = dict(zip(lit[:count_pass], list('.' * count_pass)))
    #     row = 0
    #     flag = 0
    #     if group[2] == 'aisle':
    #         r = list(pas.keys())[::-1]
    #     else:
    #         r = list(pas.keys())
    #     print('Пассажиры ', r, pas, count_pass, ' ', group[1], ' ', group[2])
    #
    #     for seat in seats_plane:
    #
    #         row = row + 1
    #         seat_val = [seat.get(key) for key in lit[:count_pass]]
    #
    #         if list(pas.values()) == seat_val:
    #             for i in r:
    #                 seats_plane[row - 1][i] = '#'
    #             for x in list(pas.keys()):
    #                 res.append(f'{row}{x}')
    #             flag = 1
    #             print('Passengers can take seats: ', *res)
    #             break
    #     if not flag:
    #         print('Cannot fulfill passengers requirements')
    #
    #
    #     # print(lit)

    # for group in groups:
    #     pas = '.' * int(group[0])
    #     print('Пассажиры ', pas)
    #     for i in range(len(raws)):
    #         if group[1] == 'left':
    #             seats = raws[i].split('_')[0]
    #             if group[2] == 'window':
    #                 if seats.startswith(pas):
    #                     print('Помещаются')
    #                     seats = seats.replace(pas, '#' * int(group[0]), 1)
    #                     raws[i] = seats + '_' + raws[i].split('_')[1]
    #                     print('Сели: ', f'ряд {i}', raws[i])
    #                     break
    #                 else:
    #                     continue
    #             elif group[2] == 'aisle':
    #                 if seats.endswith(pas):
    #                     seats = seats[::-1].replace(pas, '#' * int(group[0]), 1)
    #                     seats = seats[::-1]
    #                     raws[i] = seats + '_' + raws[i].split('_')[1]
    #                     print('Сели: ', f'ряд {i}', raws[i])
    #                     break
    #         elif group[1] == 'right':
    #             seats = raws[i].split('_')[1]
    #             if group[2] == 'aisle':
    #                 if seats.startswith(pas):
    #                     print('Помещаются')
    #                     seats = seats.replace(pas, '#' * int(group[0]), 1)
    #                     raws[i] = raws[i].split('_')[0] + '_' + seats
    #                     print('Сели: ', f'ряд {i}', raws[i])
    #                     break
    #                 else:
    #                     continue
    #             elif group[2] == 'window':
    #                 if seats.endswith(pas):
    #                     seats = seats[::-1].replace(pas, '#' * int(group[0]), 1)
    #                     seats = seats[::-1]
    #                     raws[i] = raws[i].split('_')[0] + '_' + seats
    #                     print('Сели: ', f'ряд {i}', raws[i])
    #                     break
    #     else:
    #         print('Cannot fulfill passengers requirements')
    #
    #         # print('в ряд: ', raws[i])
    #         # if pas in raws[i]:
    #         #     print('Помещаются')
    #         #     raws[i] = raws[i].replace(pas, '#' * int(group[0]), 1)
    #         #     print('Сели: ', raws[i])
    #         #
    #         #     break
    #         # else:
    #         #     print('Cannot fulfill passengers requirements')
    # for i in seats_plane:
    #     print(*i.values())


# def main():
#     solution(RAWS, GROUPS)
#
#
# if __name__ == '__main__':
#     RAWS = ['..._.#.', '.##_...', '.#._.##', '..._...']
#     GROUPS = [['2', 'left', 'aisle'], ['3', 'right', 'window'],
#               ['2', 'left', 'window'], ['3', 'left', 'aisle'],
#               ['1', 'right', 'window'], ['2', 'right', 'window'],
#               ['1', 'right', 'window']]
#     main()

"""
4
..._.#.
.##_...
.#._.##
..._...
7
2 left aisle
3 right window
2 left window
3 left aisle
1 right window
2 right window
1 right window
"""
