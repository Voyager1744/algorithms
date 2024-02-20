"""
B. Автодополнение на минималках
Ограничение времени	2 секунды
Ограничение памяти	256.0 Мб
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан словарь из
N
N различных слов, состоящих из строчных английских букв.

Вам приходит
Q
Q запросов,
i
i-й из которых состоит из строки
p
i
p
i
​
  из строчных английских букв и числа
k
i
k
i
​
 . В ответ на
i
i-й запрос вы должны вывести
k
i
k
i
​
 -е в лексикографическом порядке слово из словаря среди слов, имеющих
p
i
p
i
​
  в качестве префикса.

Формат ввода
В первой строке ввода находятся числа
N
N и
Q
Q (
1
≤
N
≤
3
⋅
1
0
5
,
1
≤
Q
≤
5
⋅
1
0
3
1≤N≤3⋅10
5
 ,1≤Q≤5⋅10
3
 ) — размер словаря и количество запросов.

В
i
i-й из следующих
N
N строк находится единственная строка
w
i
w
i
​
  (
1
≤
∣
w
i
∣
≤
2
⋅
1
0
6
1≤∣w
i
​
 ∣≤2⋅10
6
 ) из строчных английских букв —
i
i-е слово из словаря.

Гарантируется, что:

суммарная длина слов из словаря не превосходит
2
⋅
1
0
6
2⋅10
6

слова отсортированы в лексикографическом порядке
слова в словаре различны
В следующих
Q
Q строках находятся запросы. Каждый запрос описывается целым числом
k
i
k
i
​
  (
1
≤
k
i
≤
1
0
9
1≤k
i
​
 ≤10
9
 ) и строкой
p
i
p
i
​
  из строчных английских букв (
1
≤
∣
p
i
∣
≤
1
0
3
1≤∣p
i
​
 ∣≤10
3
 ).

Формат вывода
Выведите
Q
Q строк,
i
i-я из которых должна содержать ответ на
i
i-й запрос. Если подходящая строка существует, то выведите её порядковый номер в словаре. Иначе выведите
−
1
−1.
"""


# def binary_search_first(words, prefix):
#     left, right = 0, len(words) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if words[mid][0].startswith(prefix):
#             right = mid - 1
#         else:
#             left = mid + 1
#     return left
#
#
# def binary_search_last(words, prefix):
#     left, right = 0, len(words) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if words[mid][0].startswith(prefix):
#             left = mid + 1
#         else:
#             right = mid - 1
#     return right
#
#
# if __name__ == "__main__":
#     N, Q = map(int, input().split())
#     words = [(input().strip(), i) for i in range(1, N + 1)]
#     words.sort()
#
#     for _ in range(Q):
#         k, p = input().split()
#         k = int(k)
#
#         start_index = binary_search_first(words, p)
#         end_index = binary_search_last(words, p)
#
#         if start_index <= end_index and start_index + k - 1 <= end_index:
#             print(words[start_index + k - 1][1])
#         else:
#             print("-1")

import hashlib

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.index = -1
        self.prefix_hash = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        node = self.root
        prefix_hash = ""
        for char in word:
            prefix_hash = hashlib.sha256((prefix_hash + char).encode()).hexdigest()
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_hash = prefix_hash
        node.end_of_word = True
        node.index = index

    def search(self, prefix):
        node = self.root
        prefix_hash = ""
        for char in prefix:
            prefix_hash = hashlib.sha256((prefix_hash + char).encode()).hexdigest()
            if char not in node.children:
                return []
            node = node.children[char]
            if node.prefix_hash != prefix_hash:
                return []
        return self._find_words(node)

    def _find_words(self, node):
        result = []
        if node.end_of_word:
            result.append(node.index)
        for child in node.children.values():
            result.extend(self._find_words(child))
        return result


if __name__ == "__main__":
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]

    trie = Trie()
    for index, word in enumerate(words, start=1):
        trie.insert(word, index)

    for _ in range(Q):
        k, p = input().split()
        k = int(k)
        found_words_indices = trie.search(p)
        if len(found_words_indices) >= k:
            print(found_words_indices[k - 1])
        else:
            print("-1")
