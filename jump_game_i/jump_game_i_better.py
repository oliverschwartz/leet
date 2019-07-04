class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        maxSteps = nums[0]

        # edge case - we start on 0 so will never get to end
        if maxSteps == 0 and len(nums) > 1: return False
        
        # greedily walk to the right. At each new index, take the maximum
        # number of steps available
        for i in range(1, n - 1):
            maxSteps = max(maxSteps - 1, nums[i])
            if maxSteps == 0: return False
        return True