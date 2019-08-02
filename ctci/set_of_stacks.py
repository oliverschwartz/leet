class EmptyStackException(Exception):
    pass

class NoSuchStack(Exception):
    pass

class Stack:
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size
        self.count = 0
    def push(self, x):
        self.data.append(x)
        self.count += 1
    def pop(self):
        if self.count == 0:
            raise EmptyStackException
        else:
            self.count -= 1
            return self.data.pop()
    def empty(self):
        return self.count == 0
    def full(self):
        return self.count == self.max_size

"""Note - assumes we're okay with not every stack being at full
capacity as an invariant"""

class StackSet:
    def __init__(self, max_size):
        self.stacks = [Stack(max_size)]
        self.max_size = max_size
        self.active_stack = self.stacks[0]
    def push(self, x):
        if self.active_stack.full():
            self.stacks.append(Stack(self.max_size))
            self.active_stack = self.stacks[-1]
        self.active_stack.push(x)
    def pop(self):
        if self.active_stack.empty() and len(self.stacks) == 1:
            raise EmptyStackException
        elif self.active_stack.empty() and len(self.stacks) > 1:
            self.stacks.pop()
            self.active_stack = self.stacks[-1]
        return self.active_stack.pop()
    def empty(self):
        return len(self.stacks) == 1 and self.active_stack.empty()
    def popAt(self, idx):
        if idx > len(self.stacks) - 1:
            raise NoSuchStack
        else:
            self.active_stack = self.stacks[idx]
            val = self.active_stack.pop()
            if self.active_stack.empty():
                self.stacks.pop(idx)
            self.active_stack = self.stacks[-1]
            return val
