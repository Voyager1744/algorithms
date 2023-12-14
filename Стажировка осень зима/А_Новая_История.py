"""
Сейчас активно развивается новая история, основателем которой является Профессор А.С. Багиров.
Он выяснил, что на протяжении многих лет на земле вместе с людьми существовали ящеры. Строительство
пирамид, захват Байкала и еще много разных событий произошли благодаря ящерам.
Учёные ещё не выяснили, сколько времени ящеры существовали на земле. Они находят разные данные в
виде даты начала и даты окончания, и чтобы проверить их на корректность, необходимо посчитать,
сколько дней ящеры существовали для двух конкретных дат. Календарь ящеров очень похож на
григорианский, лишь с тем исключением, что там нет високосных годов.
Вам даны дата начала и дата окончания существования ящеров, нужно найти количество полных дней
и секунд в неполном дне, чтобы учёные смогли оценить, насколько даты корректны.
"""


def count_days(date1: list, date2: list) -> list:
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def seconds_since_epoch(date):
        year, month, day, hour, minute, second = date
        days_in_year = year * 365 + sum(months[:month]) + day - 1
        seconds_in_hour = hour * 60 * 60
        seconds_in_minute = minute * 60
        return (
            days_in_year * 24 * 60 * 60 + seconds_in_hour + seconds_in_minute + second
        )

    sec_in_data1 = seconds_since_epoch(date1)
    sec_in_data2 = seconds_since_epoch(date2)

    res = sec_in_data2 - sec_in_data1
    res_days = res // (24 * 60 * 60)
    res_sec = res % (24 * 60 * 60)

    return [res_days, res_sec]


data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

print(*count_days(data1, data2))
