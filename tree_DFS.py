"""
Задача. Дано бинарное дерево, нужно вывести список списков значений
вершин «по слоям». В каждом слое значения должны идти слева направо.
Для дерева:
     5
    / \
   /   \
  3     1
   \   /
    4 2
нужно вернуть
[[5], [3, 1], [4, 2]]

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Banch(dict):
    def __init__(self, *args, **kwargs):
        super(Banch, self).__init__(*args, **kwargs)
        self.__dict__ = self


def get_layered_representation(root):
    result = []
    DFS(root, 0, result)
    return result


def DFS(node, depth, result):
    if not node:
        return
    # Т.к. мы выбрали preorder, то результат нужно увеличивать
    # не больше, чем на 1
    if depth >= len(result):
        result.append([])
    result[depth].append(node.val)
    DFS(node.left, depth + 1, result)
    DFS(node.right, depth + 1, result)
