"""
Linked List nad Array Running time Complexity
-> Insert_start
-> Insert End
Inserting items into Linked List in 1.3034343719482422s
Inserting items into Array in 61.44821357727051s
"""
import time


class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numberOfNodes = 0

    # This is linked list // O(1)  time complexity
    def insert_start(self, data):
        self.numberOfNodes = self.numberOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # lienar running time - O(N)
    def insert_end(self, data):
        self.numberOfNodes = self.numberOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def remove(self, data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        # Search - the item is not  present is the linked list
        if actual_node is None:
            return

        self.numberOfNodes = self.numberOfNodes - 1

        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode

    def size_of_list(self):
        return self.numberOfNodes

    # Linear time complexity - O(N)
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode


if __name__ == '__main__':
    ll = LinkedList()
    now = time.time()

    for i in range(400000):
        ll.insert_start(i)

    print("Inserting items into Linked List in %ss" % str(time.time() - now))

    array = []
    now = time.time()
    for i in range(400000):
        array.insert(0, i)

    print("Inserting items into Array in %ss" % str(time.time() - now))
