N = int(input())
p = list(map(int, input().split()))


days = [i for i in range(1, N + 1)]

days_prices = dict(zip(days, p))

deals = []
buy_days = []
sell_days = []
res = 0
buy = 0

for i in range(1, N):
    price_today = days_prices[i]
    if days_prices[i + 1] >= price_today:
        if not buy:
            buy_days.append(i)
        buy = 1
        price_today = days_prices[i + 1]
    else:
        if buy:
            sell_days.append(i)
            buy = 0
if buy:
    sell_days.append(N)

deals = list(zip(buy_days, sell_days))
print(buy_days, sell_days)
print(deals)

results = {}

for b, s in deals:
    res = days_prices[s] - days_prices[b]
    results[(b, s)] = res

sorted_results = dict(sorted(results.items(), key=lambda x: x[1]))

res_days = list(sorted_results.keys())[-2:]

print(len(res_days))
for days in res_days:
    print(*days)


for i in buy_days:
    for j in sell_days:
        if j > i:
            profit = days_prices[j] - days_prices[i]
            results[(i, j)] = profit

            print(f"покупка в {i} день продажа в  {j} день, прибыль = {profit}")

print(results.values())

"""
11
1 3 2 6 4 5 2 5 4 9 5
"""
