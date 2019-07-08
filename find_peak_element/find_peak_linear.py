class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        n1 = -float('inf')
        n2 = nums[0]
        for i in range(1,  n):
            n3 = nums[i]
            if n1 < n2 and n2 > n3:
                return i - 1
            else:
                n1 = n2
                n2 = n3
        
        # if we got to end, need to return last elt
        return n - 1