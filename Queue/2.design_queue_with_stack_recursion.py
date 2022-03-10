"""
Queue with stack problem
The aim is to design a queue abstract data type with the help of stacks.

enqueue () and dequeue() operations
--> we can use 2 stacks
--> but we use one stack for recurssion
"""


# First in First Out
class DesignQueue:

    def __init__(self):
        # Use one stack for enqueue  and dequeue operation
        self.stack = []

    # adding items into the queue is O(1) operation
    def enqueue(self, data):
        self.stack.append(data)

    # Note: we use 2 stacks again but instead of explicitly define the second stack
    # we use the class- stack of program(stack memeory or execution stack)
    def dequeue(self):
        # Base case for the reursive method calls the first item is what weare after
        if len(self.stack) == 1:
            return self.stack.pop()

        # we keep popping the item until we find the last one
        item = self.stack.pop()

        # we call the method recursively untill we find the fiorst items we have
        # inserted
        dequeued_item = self.dequeue()

        # after we find the item we have to reinsert the items one by one
        self.stack.append(item)

        # this is the item we are looking for (this is what have been popped off in the stack.size()==1 section)
        return dequeued_item


if __name__ == '__main__':
    q = DesignQueue()
    q.enqueue(12)
    q.enqueue(23)
    q.enqueue(542)
    q.enqueue(243)
    print(q.dequeue())
    print(q.dequeue())

