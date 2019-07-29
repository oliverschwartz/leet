"""This version implements O(n) push w/ O(1) pops
"""

class MyQueue:
    
    class Stack:
        def __init__(self):
            self.stack = []
        def pop(self):
            return self.stack.pop() if self.stack != [] else None
        def peek(self):
            return self.stack[-1] if self.stack != [] else None
        def push(self, val):
            self.stack.append(val)
        def empty(self):
            return self.stack == []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.reverse = self.Stack()
        self.queue = self.Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        # move queue into a reversed version
        while not self.queue.empty():
            self.reverse.push(self.queue.pop())
            
        # push x onto reversed version
        self.reverse.push(x)
        
        # move reversed back into queue
        while not self.reverse.empty():
            self.queue.push(self.reverse.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""This version implements O(n1) push w/ O(1) amortized pops
"""

class MyQueue:
    
    class Stack:
        def __init__(self):
            self.stack = []
        def pop(self):
            return self.stack.pop() if self.stack != [] else None
        def peek(self):
            return self.stack[-1] if self.stack != [] else None
        def push(self, val):
            self.stack.append(val)
        def empty(self):
            return self.stack == []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.reverse = self.Stack()
        self.queue = self.Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.reverse.push(x)

    def __build_queue(self):
        while not self.reverse.empty():
            self.queue.push(self.reverse.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        # reverse if we must
        if self.queue.empty():
            self.__build_queue()
            
        return self.queue.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        # reverse if we must
        if self.queue.empty():
            self.__build_queue()
            
        return self.queue.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (self.queue.empty() and self.reverse.empty())
        