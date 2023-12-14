"""Вася решил обработать логи с сервера, но обнаружил, что из-за ошибки
разработчиков для каждого события в логе записывается только время этого
события в формате HH:MM:SS, а дата не записывается. Известно, что все события
записаны в хронологическом порядке и два события не могли произойти в одну и
ту же секунду. Определите минимальное количество дней, в течение которых
записывался лог."""

n = int(input())
times = []
for _ in range(n):
    time = input().split(":")
    times.append((int(time[0]), int(time[1]), int(time[2])))

days_count = 1
prev_time = None

for time in times:
    if prev_time is None:
        prev_time = time
    elif time <= prev_time:
        days_count += 1

    prev_time = time

print(days_count)
