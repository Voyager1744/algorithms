n = int(input())
times = []
for _ in range(n):
    time = input().split(':')
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
