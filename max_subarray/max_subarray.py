class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        
        dynamic = 0
        for i in range(n):
            dynamic += nums[i]
            
            # might have found a new best
            if dynamic > 0: max_val = max(dynamic, max_val)
                
            # reset dynamic counter, since no point adding a negative
            else: dynamic = 0
    
        return max_val