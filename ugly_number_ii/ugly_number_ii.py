import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        
        heap = [1]
        visited = {1}
        
        for i in range(n):
            val = heapq.heappop(heap)
            
            for newval in [val * 2, val * 3, val * 5]:
                if newval not in visited:
                    visited.add(newval)
                    heapq.heappush(heap, newval)
                
            
        return val
        