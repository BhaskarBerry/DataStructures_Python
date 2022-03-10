"""
Binary Search Tree
"""


class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BST:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def remove_node(self, data, node):
        # we have to find the node we have to remove
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:
            # we have found the node we want to remove
            # there are 3 options
            # LEAF NODE CASE
            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf node.. %d" % node.data)
                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            # WHEN THERE IS A SINGLE CHILD
            elif node.leftChild is None and node.rightChild is None:
                print("Removing a node with single right child..")
                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = node.rightChild
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = node.rightChild

                if parent is None:
                    self.root = node.rightChild

                node.rightChild.parent = parent

                del node

            # WHEN THERE IS A SINGLE CHILD
            elif node.leftChild is None and node.rightChild is None:
                print("Removing a node with single left child..")
                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild

                else:
                    self.root = node.left_node

                node.leftChild.parent = parent

                del node
            # When Node with 2 children
            else:
                print("Removing node with 2 children ...")
                predecessor = self.get_predecessor(node.leftChild)

                # swap the node and predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)

        return node

    def insert_node(self, data, node):

        # we have to go to the left subtree
        if data < node.data:
            if node.leftChild is not None:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        # we have to go to right sub tree
        else:
            if node.rightChild is not None:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        # Using recursion
        # if node.rightChild:
        #     return self.get_max(node.rightChild)
        #
        # return node.data

        # Using iteration
        actual = self.root

        while actual.rightChild is not None:
            actual = actual.rightChild

        return actual.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.leftChild is not None:
            self.traverse_in_order(node.leftChild)
        print("%s" % node.data)

        if node.rightChild is not None:
            self.traverse_in_order(node.rightChild)


if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(12)
    bst.insert(-5)

    bst.remove(5)
    bst.remove(8)
    bst.remove(10)
    bst.remove(12)
    bst.traverse()
    print("----------------")
    # print("Max item : %d"% bst.get_max_value())
    # print("Max item : %d"% bst.get_max(bst.root))
    # print("Min item : %d"% bst.get_min(bst.root))
    # print()
