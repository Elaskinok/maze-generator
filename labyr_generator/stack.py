"""Module which provides interface of stack. List used in core."""


class Stack:
    """"""

    def __init__(self):
        self.stack = []

    def push(self, elem: object) -> None:
        """Add elem into top of stack."""
        self.stack.append(elem)

    def top(self) -> object:
        """Take elem from top of stack. (Do not remove elem from stack)"""
        return self.stack[-1]

    def pop(self) -> object:
        """Take elem from top of stack. (Remove elem from stack)"""
        return self.stack.pop()

    def is_empty(self) -> bool:
        """Check stack for emptiness."""
        return True if not self.stack else False
