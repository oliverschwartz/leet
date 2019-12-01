class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lengths = [1 for num in nums]
        numslen = len(nums)
        
        for i in range(numslen - 2, -1, -1):
            for j in range(i + 1, numslen):
                if nums[i] < nums[j] and lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
        print(lengths)
        
        return max(lengths)
