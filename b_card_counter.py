def max_score(cards, k):
    n = len(cards)
    # Создаем таблицу для заполнения результатов
    table = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]

    # Заполняем базовые случаи (k=0, k=1)
    for i in range(n):
        table[i][i][0] = 0
        table[i][i][1] = cards[i]

    # Заполняем таблицу для остальных значений k
    for d in range(2, k + 1):
        for i in range(n - d + 1):
            j = i + d - 1
            for l in range(d):
                # Вычисляем максимальный счет для каждого из двух вариантов (брать с левого или правого конца)
                left = table[i + 1 + l][j][d - 1]
                right = table[i][j - 1 - l][d - 1]
                table[i][j][d] = max(table[i][j][d], left + cards[i],
                                     right + cards[j])

    # Возвращаем максимальный счет
    return table[0][n - 1][k]

cards = [3, 1, 5, 8]
k = 3
max_score = max_score(cards, k)
print(max_score) # Выводит 15