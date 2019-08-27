class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xored = 0
        for n in nums:
            xored ^= n
        return xored
        
