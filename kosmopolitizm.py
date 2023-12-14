N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
Q = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = list(map(int, input().split()))

print(N)
print(a)
print(b)
print(c)
print(Q)
print(x)
print(y)
print(z)

con_for_man = []
countries_num = [x for x in range(1, N + 1)]
print("countries_num ", countries_num)
res = []
for i in range(Q):
    print(z[i])
    if z[i] in countries_num:
        con_for_man.append(z[i])
    res.append(con_for_man)


print(res)
