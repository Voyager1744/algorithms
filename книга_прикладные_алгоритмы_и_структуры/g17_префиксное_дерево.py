class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    """ Отслеживает корневой узел дерева """

    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None

        return current_node

    def insert(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node

        current_node.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]):

        # Этот метод принимает три аргумента. Первый - это узел (поdе),
        # из значений потомков которого мы собираем слова.
        # Второй аргумент, word, - изначально пустая строка,
        # куда мы добавляем символы по мере продвижения по дереву.
        # Третий аргумент, words, - изначально пустой массив,
        # а по завершении работы функции будет содержать все слова
        # из префиксного дерева.
        # Текущий узел, curreпt поdе, - это узел, переданный в качестве первого # параметра,
        # или корневой узел, если конкретное значение не указано: curreпtNode = поdе or self.root
        # Перебираем все дочерние элементы текущего узла: for key, childNode iп curreпtNode.childreп.items():
        # Если текущий ключ - *, значит, мы достигли конца # слова и можем добавить его в массив words:

        current_node = node or self.root

        for key, childNode in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)

        return words

    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.collectAllWords(current_node)



