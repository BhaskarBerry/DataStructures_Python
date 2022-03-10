# FIFO : First in first out
"""
Queue Operation : ENQUEUE, DEQUEUE, PEEK
[10.20.30.40.50.60]

"""
class Queue:

    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    # Size of queue
    def queue_size(self):
        return (len(self.queue))

    # this operation has O(1)  running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time . How to solve this problem > By using linked lIst , Doubly Lined ListO(1)
    def dequeue(self):
        if self.queue_size() < 1:
            return  -1

        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        if self.queue_size() < 1:
            return -1

        return self.queue[0]


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    print("Size of Queue: %d "%q.queue_size())
    print("Enqueue : %d"%q.dequeue())

    print("Size of Queue: %d "%q.queue_size())
    print("Enqueue : %d"%q.dequeue())

    print("Size of Queue: %d "%q.queue_size())
    print("Enqueue : %d"%q.dequeue())

    print("Size of Queue: %d "%q.queue_size())
    print("Enqueue : %d"%q.peek())

    print("Size of Queue: %d "%q.queue_size())
    print("Enqueue : %d"%q.dequeue())

    print("Size of Queue: %d "%q.queue_size())
    print("Enqueue : %d"%q.dequeue())
