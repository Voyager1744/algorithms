class Node:
    def __init__(self, data, next_node, prev_node):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return f"({self.data}, {self.next_node}, {self.prev_node})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data, None, self.tail)
            self.tail = self.tail.next_node

    def remove_from_front(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None

    def print_revesed_elements(self):
        current = self.tail
        while current is not None:
            print(current.data)
            current = current.prev_node



class Queue:
    def __init__(self):
        self.doubly_linked_list = DoublyLinkedList()

    def enqueue(self, data):
        self.doubly_linked_list.add(data)

    def dequeue(self):
        self.doubly_linked_list.remove_from_front()

    def read(self):
        return self.doubly_linked_list.head.data if self.doubly_linked_list.head is not None else None





