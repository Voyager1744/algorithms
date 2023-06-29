n = int(input())
categories = {}

for _ in range(n):
    product_id, category_id = map(int, input().split())
    if category_id not in categories:
        categories[category_id] = []
    categories[category_id].append(product_id)

order = list(map(int, input().split()))

diversity = n

for category in categories.values():
    category.sort()
    for i in range(1, len(category)):
        diff = abs(order.index(category[i]) - order.index(category[i-1]))
        diversity = min(diversity, diff)

print(diversity)

