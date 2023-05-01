"""
Поиск в ширину (BFS, Breadth-First Search) - это алгоритм обхода графа, который
на каждой итерации посещает все вершины на определенном расстоянии от стартовой
вершины, затем продвигается на следующий уровень. Это означает, что алгоритм
начинает с вершины, которую нужно посетить, и проходит по всем вершинам на
расстоянии 1 от этой вершины, затем по всем вершинам на расстоянии 2 и т.д.

BFS начинает с добавления стартовой вершины в очередь, затем повторяет следующий
шаг, пока очередь не будет пуста:

1. Извлечь первую вершину из очереди
2. Посетить все соседние вершины, которые еще не были посещены, и добавить их в
конец очереди.
Каждая вершина помечается как посещенная при извлечении из очереди. Таким
образом, вершины посещаются по уровням, начиная с вершины,
которую нужно посетить.

BFS может быть использован для нахождения кратчайшего пути в невзвешенном графе.
Если граф взвешенный, тогда вместо обычной очереди следует использовать очередь
с приоритетом, чтобы обрабатывать вершины в порядке возрастания веса.

Пример реализации алгоритма BFS на языке Python:
"""

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph[vertex]
            queue.extend(neighbors - visited)
    return visited


"""
В этом примере функция bfs принимает на вход граф в виде словаря, где ключами 
являются вершины, а значениями - списки смежных вершин. Алгоритм начинает с 
добавления стартовой вершины в очередь queue, а также создания множества visited 
для хранения посещенных вершин. Затем он запускает цикл, пока очередь не станет 
пустой. На каждой итерации алгоритм извлекает первую вершину из очереди и 
добавляет ее в множество visited. Затем он получает список смежных вершин и 
добавляет их в конец очереди, только если они еще не были посещены. В конце 
функция возвращает множество visited.
"""