import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        return value

if __name__ == "__main__":
    linked_list = LinkedList()
    for _ in range(10):
        linked_list.add_last(random.randint(1, 100))
    
    print("Liste:")
    linked_list.display()
    print("Länge der Liste:", linked_list.length())
    
    print("Iterieren durch die Liste:")
    for value in linked_list:
        print(value, end=" ")
