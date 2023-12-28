N, M, Q = map(int, input().split())

child_count = list(map(int, input().split()))

friends = {i + 1: [] for i in range(N)}

for _ in range(M):
    v, u = map(int, input().split())
    friends[v].append(u)
    friends[u].append(v)


for _ in range(Q):
    q = input().split()
    if q[0] == '?':
        print(child_count[int(q[1]) - 1])
    elif q[0] == '+':
        v, x = map(int, q[1:])
        for friend in friends[v]:
            child_count[friend - 1] += x

"""
5 5 5
1 2 3 4 5
1 2
2 3
3 4
4 5
5 1
? 1
? 5
+ 1 2
? 1
? 5

"""