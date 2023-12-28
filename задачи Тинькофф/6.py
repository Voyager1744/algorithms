def process_queries(n, q, a, queries):
    result = []
    for query in queries:
        if query[0] == '+':
            l, r, x = map(int, query[1:])
            for i in range(l - 1, r):
                a[i] += x
        elif query[0] == '?':
            l, r, k, b = map(int, query[1:])
            min_val = float('inf')
            for i in range(l - 1, r):
                min_val = min(min_val, k * (i + 1) + b + a[i])
            result.append(min_val)
    return result


n, q = map(int, input().split())
a = list(map(int, input().split()))

queries = []
for _ in range(q):
    queries.append(input().split())


result = process_queries(n, q, a, queries)


for res in result:
    print(res)


"""
6 3
2 4 6 8 10 12
? 2 5 3 0
+ 2 3 6
? 2 5 3 2

"""