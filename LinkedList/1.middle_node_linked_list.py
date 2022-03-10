"""
Finding the middle node in a linked list overview

Suppose we have a standard linked list. Construct an in-place (without extra memory)
algorithm thats able to find the middle node!
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numberOfNodes = 0

    # N/2 --->O(N) Linear time running complexity
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer

    # This is linked list // O(1)  time complexity
    def insert(self, data):
        self.numberOfNodes = self.numberOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    ll.insert(50)

    print(ll.get_middle_node().data)
