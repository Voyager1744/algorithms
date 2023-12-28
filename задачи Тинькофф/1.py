def count_char(word):
    res = {}
    for char in word:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

bord = count_char("TINKOFF")

N = int(input())
for _ in range(N):
    word = input()
    if count_char(word) == bord:
        print("Yes")
    else:
        print("No")
