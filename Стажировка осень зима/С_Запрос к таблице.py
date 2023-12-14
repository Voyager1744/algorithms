"""
Петя, стажер в Яндексе, решает SQL-задачу. У него таблица
N
×
M
и
Q
запросов. Необходимо подсчитать сумму значений в строках, соответствующих всем условиям.
Если ни одна строка не удовлетворяет всем условиям — вывести 0.

ввод
N M Q (1≤N×M≤3⋅10^5, 1≤Q≤10^5)
M имена столбцов (1≤L≤10)
N строк, каждая с M числами (-10^9≤aij≤10^9)
Q запросов в формате "Column_Namek qk valk" (qk∈(<,>), -10^9≤valk≤10^9)

вывод
S - сумма чисел в строках, удовлетворяющих всем условиям запросов.
Если ни одна строка не соответствует всем условиям, вывести 0.


"""


def satisfies_constraints(row, constraints):
    for col_index, op, val in constraints:
        if op == "<" and row[col_index] >= val:
            return False
        elif op == ">" and row[col_index] <= val:
            return False
    return True


N, M, Q = map(int, input().split())
columns = input().split()
col_indices = {col: i for i, col in enumerate(columns)}
table = [list(map(int, input().split())) for _ in range(N)]


constraints = []
for _ in range(Q):
    query = input().split()
    col_name, op, val = query[0], query[1], int(query[2])
    col_index = col_indices[col_name]
    constraints.append((col_index, op, val))


valid_rows = set(range(N))


for col_index, op, val in constraints:
    if op == "<":
        valid_rows = {i for i in valid_rows if table[i][col_index] < val}
    elif op == ">":
        valid_rows = {i for i in valid_rows if table[i][col_index] > val}


result_sum = sum(sum(table[i]) for i in valid_rows)


print(result_sum)

# Частичное решение. TL на 32 тесте
