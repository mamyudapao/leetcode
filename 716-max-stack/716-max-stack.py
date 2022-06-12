class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        max = self.peekMax()
        reverse = self.stack[::-1]
        index = reverse.index(max)
        return self.stack.pop(len(self.stack)-1-index)
