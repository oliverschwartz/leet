class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # memoize our answers in the format 
        # where memo[idx][prev] gives the value of calling
        # recurseLIS(idx, prev)
        memo = [{} for i in range(n)]
        
        def recurseLIS(idx, prev):
            """Recursive helper function that tells us the maximum increasing 
            sublist starting at idx, with previous element prev"""
            
            # recursive base case for empty list
            if idx == n: return 0
            
            # use memoization if we can
            if prev in memo[idx]: return memo[idx][prev]
            
            # otherwise we recurse to starting at idx + 1, taking the max
            # of whether or not we include nums[idx]
            memo[idx][prev] = max(
                # if we don't include nums[idx]
                # in this case prev stays the same
                recurseLIS(idx + 1, prev),

                # if we do include nums[0] - only possible if its > prev
                # in this case the new prev is nums[0]
                1 + recurseLIS(idx + 1, nums[idx]) if nums[idx] > prev else 0
            )
            return memo[idx][prev]

        return recurseLIS(0, -float('inf'))

                