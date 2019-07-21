class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        heap = [1]
        visited = {1}
        
        for i in range(n):
            val = heapq.heappop(heap)
            for p in primes:
                if val * p not in visited:
                    visited.add(val * p)
                    heapq.heappush(heap, val * p)
            
        return val