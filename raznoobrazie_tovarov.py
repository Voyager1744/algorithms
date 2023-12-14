n = int(input())
categories = {}
product_ids = []

for _ in range(n):
    product_id, category_id = map(int, input().split())
    product_ids.append(product_id)
    if category_id in categories:
        categories[category_id].append(product_id)
    else:
        categories[category_id] = [product_id]

for category in categories.values():
    category.sort()

sorted_categories = sorted(
    categories.keys(), key=lambda x: len(categories[x]), reverse=True
)

result = []
while categories:
    for category in sorted_categories:
        if category in categories:
            result.append(categories[category].pop(0))
            if len(categories[category]) == 0:
                del categories[category]

for product_id in product_ids:
    if product_id not in result:
        result.append(product_id)

print(*result)
