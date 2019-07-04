class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        reachable = [False for i in range(n)]
        reachable[0] = True
        
        for i in range(n):
            if reachable[i]:
                steps = nums[i]
                reachable[i + 1 : i + steps + 1] = [True] * steps
                
        return reachable[n - 1]