import heapq

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        gt = [-1 for i in range(n)]
        
        to_set = []
        for i in range(2 * n):
            while to_set and to_set[0][0] < nums[i % n]:
                gt[heapq.heappop(to_set)[1]] = nums[i % n]
            heapq.heappush(to_set, (nums[i % n], i % n))
        return gt