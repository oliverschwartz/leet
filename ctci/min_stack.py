class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.current_min = float('inf')
        

    def push(self, x: int) -> None:
        self.current_min = min(self.current_min, x)
        self.stack.append((x, self.current_min))

    def pop(self) -> None:
        val = self.stack.pop()[0]
        self.current_min = self.stack[-1][1] if self.stack != [] else float('inf')
        return val

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
