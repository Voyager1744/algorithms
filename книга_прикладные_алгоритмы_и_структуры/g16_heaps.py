class Heap:
    """ Реализация кучи с помощью массива """

    def __init__(self):
        self.array = []

    def root_node(self):
        return self.array[0]

    def last_node(self):
        return self.array[-1]

    def left_child_index(self, index):
        return self.array[2 * index + 1]

    def right_child_index(self, index):
        return self.array[2 * index + 2]

    def parent_index(self, index):
        return self.array[(index - 1) // 2]

    def insert(self, value):
        self.array.append(value)
        new_node_index = len(self.array)

        while new_node_index > 0 and self.array[new_node_index] > self.parent_index(new_node_index):
            (self.parent_index(new_node_index), self.array[new_node_index] ==
             self.array[new_node_index], self.parent_index(new_node_index))

            new_node_index = self.parent_index(new_node_index)

    def delete(self):
        def has_greater_child(index):
            (self.left_child_index(index) and self.left_child_index(index) > self.array[index] or
             self.right_child_index(index) and self.right_child_index(index) > self.array[index])

        def calculate_larger_child_index(index):
            if not self.right_child_index(index):
                return self.left_child_index(index)
            if self.right_child_index(index) > self.left_child_index(index):
                return self.right_child_index(index)
            else:
                return self.left_child_index(index)

        # Из кучи всегда удаляется только корневой узел, по этому
        # извлекаем из массива последний узел и делаем его корневым

        # Следующий цикл выполняет алгоритм просачивания узла вниз:

        # Продолжаем выполнять этот цикл пока у просачивающегося узла есть
        # дочерний, значение которого превышает его собственное

        self.array[0] = self.array.pop()

        trickle_node_index = 0

        while has_greater_child(trickle_node_index):
            # Сохраняем значение большего дочернего узла в переменную
            larger_child_index = calculate_larger_child_index(trickle_node_index)

            # Если значение большего дочернего узла больше значения просачивающегося
            # узла, меняем их местами

            self.array[trickle_node_index], self.array[larger_child_index] = (
                self.array[larger_child_index], self.array[trickle_node_index]
            )
            trickle_node_index = larger_child_index
