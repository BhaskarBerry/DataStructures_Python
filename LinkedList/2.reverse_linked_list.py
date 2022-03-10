# """
# Reverse a linked list in-place overview
# Construct an in-place algorithm to reverse a linked list!
#
# """
#
#
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.nextNode = None
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.numberOfNodes = 0
#
#     # O(N) running time complexity
#     def reverse(self):
#         current_node = self.head
#         previous_node = None
#         next_node = None
#
#         while current_node is not None:
#             next_node = current_node.nextNode
#             current_node.next_node = previous_node
#             previous_node = current_node
#             current_node = next_node
#         self.head = previous_node
#
#         # return self.head
#
#     #  O(1)  time complexity
#     def insert(self, data):
#         self.numberOfNodes = self.numberOfNodes + 1
#         new_node = Node(data)
#
#         if not self.head:
#             self.head = new_node
#         else:
#             new_node.nextNode = self.head
#             self.head = new_node
#
#     def traverse_list(self):
#         actual_node = self.head
#
#         while actual_node is not None:
#             print("%d " % actual_node.data)
#             actual_node = actual_node.nextNode
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert(10)
#     ll.insert(20)
#     ll.insert(30)
#     ll.insert(40)
#     ll.insert(50)
#
#     ll.traverse_list()
#     ll.reverse()
#     print("------------")
#     ll.traverse_list()

# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
