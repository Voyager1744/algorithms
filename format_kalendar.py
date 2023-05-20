# def format_kalendar(ndays, day_week):
#     weekday = {'Monday': 0,
#                'Tuesday': 1,
#                'Wednesday': 2,
#                'Thursday': 3,
#                'Friday': 4,
#                'Saturday': 5,
#                'Sunday': 6
#                }
#
#     ndays = int(ndays)
#     days = []
#     prefix = ['..'] * weekday[day_week]
#
#     for d in range(1, ndays + 1):
#         d = str(d)
#         if len(d) == 1:
#             d = '.' + d
#         days.append(str(d))
#     if prefix:
#         days = prefix + days
#
#     table = [days[:7], days[7:14], days[14:21], days[21:28]]
#     if 28 < len(days) <= 35:
#         table.append(days[28:35])
#     if 35 < len(days) < 42:
#         table.append(days[35:])
#
#     return table
#
#
# n_days, day_week = input().split()
# for week in format_kalendar(n_days, day_week):
#     print(' '.join(map(str, week)))

# for n_days in (28, 29, 30, 31):
#     for day_week in ('Monday',
#                      'Tuesday',
#                      'Wednesday',
#                      'Thursday',
#                      'Friday',
#                      'Saturday',
#                      'Sunday'):
#
#         for week in format_kalendar(n_days, day_week):
#             print(' '.join(map(str, week)))


def format_calendar(num_days, first_day):
    weekdays = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    empty_days = weekdays[first_day]
    days = [''] * empty_days + list(range(1, num_days + 1))
    weeks = [days[i:i + 7] for i in range(0, len(days), 7)]

    for week in weeks:
        for i in range(len(week)):
            if week[i] == '':
                week[i] = '..'
            elif week[i] < 10:
                week[i] = '.' + str(week[i])

    return weeks


# Пример использования
n_days, first_day = input().split()
n_days = int(n_days)
weeks = format_calendar(n_days, first_day)

for week in weeks:
    print(' '.join(map(str, week)))
