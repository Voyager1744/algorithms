"""
Статус 200
Вам дан массив натуральных чисел ai. Найдите число таких пар элементов(ai,aj),
где∣∣ai−aj∣∣%200==0 и i<j.

"""


def get_number_of_good_pairs(numbers) -> int:
    res = 0

    mod_count = {}
    for x in numbers:
        mod = x % 200
        mod_count[mod] = mod_count.get(mod, 0) + 1

    for count in mod_count.values():
        res += count * (count - 1) // 2

    return res


n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))
