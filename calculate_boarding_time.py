def calculate_boarding_time(n, passenger_list):
    seats = [
        [False] * 6 for _ in range(31)
    ]  # Матрица для отслеживания состояния каждого места
    total_delay = 0  # Общее время задержки

    for passenger in passenger_list:
        arrival_time, seat = passenger.split()
        row = int(seat[:-1])
        column = ord(seat[-1]) - ord("A")

        # Поиск свободного места в том же ряду или следующих рядах
        next_row = row
        while next_row <= 30 and seats[next_row][column]:
            next_row += 1

        # Если найдено свободное место, посадка пассажира
        if next_row <= 30 and row < next_row:
            seats[next_row][column] = True
            delay = (next_row - row) * 10 + int(arrival_time)
            total_delay += delay

    return total_delay


n = int(input())  # Количество пассажиров
passenger_list = []
for _ in range(n):
    passenger_list.append(input())

boarding_time = calculate_boarding_time(n, passenger_list)
print(boarding_time)
