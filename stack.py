""""""


class Stack:
    """"""

    def __init__(self):
        self.stack = []

    def push(self, elem: object) -> None:
        self.stack.append(elem)

    def top(self) -> object:
        return self.stack[-1]

    def pop(self) -> object:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return True if not self.stack else False
