import heapq

class FreqStack(object):

    def __init__(self):
        self.push_time = 0
        self.freqs = {}
        self.freq_heap = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.freqs[x] = 1 if x not in self.freqs else self.freqs[x] + 1
        
        # heap first compares on frequency, then on time added
        # note that a separate entry is present for every frequency of x
        #
        # i.e. if x is added and freq = 2, the timestamp with that addition is stored as
        # one heap entry. Then if we add another x,
        # a new heap entry is added with a new timestamp)
        #
        x_heap_entry = (-self.freqs[x], -self.push_time, x)
        heapq.heappush(self.freq_heap, x_heap_entry)
        self.push_time += 1    

    def pop(self):
        """
        :rtype: int
        """
        (freq, time, x) = heapq.heappop(self.freq_heap)
        self.freqs[x] -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()