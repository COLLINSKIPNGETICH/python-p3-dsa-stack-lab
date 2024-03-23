class Stack:
    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.elements.pop()

    def peek(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.elements[-1]
