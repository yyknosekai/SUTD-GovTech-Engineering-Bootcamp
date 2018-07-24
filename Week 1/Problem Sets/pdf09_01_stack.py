class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self.empty():
            return self._stack.pop()
        else:
            raise IndexError('Stack is empty.')

    def top(self):
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def empty(self):
        return self.size() == 0
