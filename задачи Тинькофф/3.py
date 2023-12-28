def can_remain_after_shopping(credit, gift_prices, n):
    remaining_money = credit
    items_bought = 0

    for price in gift_prices:
        if price <= remaining_money:
            remaining_money -= price
            items_bought += 1
        if items_bought == n:  # Если Максим купил все товары, прерываем цикл
            break

    return items_bought


def find_max_remaining_money(n, m, gift_prices):
    left, right = 0, m
    max_remaining_money = 0

    while left <= right:
        mid = (left + right) // 2
        items_bought = can_remain_after_shopping(mid, gift_prices, n)

        if items_bought == n:
            max_remaining_money = max(max_remaining_money, m - mid)
            left = mid + 1
        else:
            right = mid - 1

    return max_remaining_money


# Чтение входных данных
n, m = map(int, input().split())
gift_prices = list(map(int, input().split()))

# Поиск максимального остатка денег
result = find_max_remaining_money(n, m, gift_prices)

# Вывод результата
print(result)
