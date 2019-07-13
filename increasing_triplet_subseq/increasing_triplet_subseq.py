class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2: return False
        
        # these track the smallest, and next biggest numbers we've seen
        smallest = nums[0]
        next_biggest = float('inf')
        
        for n in nums:
            # found an increasing triplet
            if n > next_biggest: return True
            
            # found a new smallest
            elif n < smallest: smallest = n
                
            # found a new next_biggest
            elif smallest < n < next_biggest: next_biggest = n
        
        return False
