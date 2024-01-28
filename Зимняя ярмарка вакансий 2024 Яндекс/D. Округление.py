def find_sum(a):
    return sum(a)

def divide_b(b, sum_a):
    return [b_i / sum_a for b_i in b]

def find_c(b, x):
    n = len(b)
    c = [0] * n
    c[0] = x
    for i in range(1, n):
        c[i] = c[i - 1] + b[i]
        if c[i] > x:
            c[i] = c[i - 1]
    return c

def find_c_sequence(a, x):
    sum_a = find_sum(a)
    b = divide_b(a, sum_a)
    return find_c(b, x)


# Чтение ввода
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Вывод результатов
result = find_c_sequence(a, x)
print(*result)
