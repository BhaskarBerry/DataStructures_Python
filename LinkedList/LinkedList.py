"""
Linked List
-> Insert_start
-> Insert End

"""


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

        self.numberOfNodes = self.numberOfNodes -1
        
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


ll = LinkedList()

ll.insert_start(4)
ll.insert_start(5)
ll.insert_start(6)
ll.insert_end(12)
ll.insert_end(120)
ll.traverse()
print("Size of Linked List : ", ll.size_of_list())
ll.remove(4)
print("Size of Linked List : ", ll.size_of_list())
print("-----------------")
ll.traverse()
