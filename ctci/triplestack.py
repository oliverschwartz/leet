
class EmptyException(Exception):
    pass

STACK_SIZE = 5

class TripleStack:
    def __init__(self, STACK_SIZE):
        self.size = STACK_SIZE
        self.data = [None] * self.size * 3
        self.stack_ptrs = {
            1: 0,
            2: self.size,
            3: 2 * self.size
        }

    def grow_stack(self):
        self.data = (
            self.data[: self.size] +
            [None] * self.size +
            self.data[self.size : 2 * self.size] +
            [None] * self.size + 
            self.data[2 * self.size :] +
            [None] * self.size
        )
        self.stack_ptrs = {
            1: self.stack_ptrs[1],
            2: self.stack_ptrs[2] + self.size,
            3: self.stack_ptrs[3] + 2 * self.size
        }
        self.size *= 2

    def push(self, stack, val):
        if self.stack_ptrs[stack] == stack * self.size - 1:
            self.grow_stack()
        if self.data[self.stack_ptrs[stack]] is not None:
            self.stack_ptrs[stack] += 1
        self.data[self.stack_ptrs[stack]] = val

    def pop(self, stack):
        if self.stack_ptrs[stack] == (stack - 1) * self.size:
            raise EmptyException
        else:
            val = self.data[self.stack_ptrs[stack]]
            self.stack_ptrs[stack] -= 1
            return val
