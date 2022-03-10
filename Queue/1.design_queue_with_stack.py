"""
Queue with stack problem
The aim is to design a queue abstract data type with the help of stacks.
"""


class DesignQueue:

    def __init__(self):
        # Use one stack for enqueue operation
        self.stack_enqueue = []
        # use one stack for dequeue operation
        self.stack_dequeue = []

    # adding items into the queue is O(1) operation
    def enqueue(self, data):
        self.stack_enqueue.append(data)

    # getting items
    def dequeue(self):

        # when there is no item in the stack
        if len(self.stack_enqueue) == 0 and len(self.stack_dequeue) == 0:
            raise Exception("Stacks are empty")

        # if the dequeue is empty we have to add items in O(N) time
        if len(self.stack_dequeue) == 0:
            while len(self.stack_enqueue) != 0:
                self.stack_dequeue.append((self.stack_enqueue.pop()))

        # otherwise we have to just pop ff an item in O(1)
        return self.stack_dequeue.pop()


if __name__ == '__main__':
    q = DesignQueue()
    # q.enqueue(12)
    # q.enqueue(23)
    # q.enqueue(542)
    # q.enqueue(243)
    print(q.dequeue())

