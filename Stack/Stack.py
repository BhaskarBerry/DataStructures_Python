# LIFO : Last in First Out
"""
LIFO- Stack operation : PUSH, POP, PEEK
[1,2,3,4,5]

"""


class Stack:

    def __init__(self):
        self.stack = []

    # Insert items into the stack -- O(1)
    def push(self, data):
        self.stack.append(data)

    # Return top item from the stack and removes it -- O(1)
    def pop(self):
        if self.stack_size() < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # Peek: It returns the last item without removing it -- O(1)
    def peek(self):
        if self.stack_size() < 1:
            return -1
        return self.stack[-1]

    # Has O(1) running time
    def is_empty(self):
        return self.stack == []

    # It return the length of teh stack size;
    def stack_size(self):
        return len(self.stack)


if __name__ == '__main__':
    s = Stack()
    print(type(s))
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print('Size: %d' % s.stack_size())
    print('Popped Item: %d' % s.pop())
    print('Size: %d' % s.stack_size())
    print('Popped Item: %d' % s.pop())
    print('Size: %d' % s.stack_size())
    print('Popped Item: %d' % s.pop())
    print('Size: %d' % s.stack_size())
    print('Popped Item: %d' % s.pop())
    print('Size: %d' % s.stack_size())
    print('Popped Item: %d' % s.pop())
    print('Size: %d' % s.stack_size())
    print("Peek Item : %d" % s.peek())
    print('Size: %d' % s.stack_size())
