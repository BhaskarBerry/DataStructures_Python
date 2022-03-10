"""
Max in a stack problem overview
The aim is to design an algorithm that can return the maximum item of a stack
in O(1) running time complexity. We can use O(N) extra memory!

Hint: we can use another stack to track the max item!
"""


class MaxStack:

    def __init__(self):
        # One stack for actual data operation
        self.main_stack = []
        # second stack for the max_data operation
        self.max_stack = []

    # Insert items into the stack -- O(1)
    def push(self, data):
        self.main_stack.append(data)

        # first items is same in both the stack
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return

        # If the iotem is largest so far: we insert it into the stack stack[-1] is the
        # peek operation: returns the last item we have inserted without removing
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            # the largest on on the max_stack is duplicated
            self.max_stack.append(self.max_stack[-1])

    # Return top item from the stack and removes it -- O(1)
    def pop(self):
        return self.main_stack.pop()

    # It return the max item we have inserted in the max_stack -- O(1)
    def get_max_item(self):
        return self.max_stack.pop()


if __name__ == '__main__':
    s = MaxStack()
    s.push(10)
    s.push(30)
    s.push(50)
    s.push(60)
    s.push(23)
    print("Maximum item in the stack : ", s.get_max_item())
    print("Maximum item in the stack : ", s.pop())
