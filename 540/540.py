class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        def helper(lo, hi):
            if lo == hi:
                return nums[lo]
            
            mid = (hi + lo) // 2
            
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            elif nums[mid] == nums[mid + 1]: 
                if (mid + 1) % 2 == 0:
                    return helper(lo, mid - 1)
                return helper(mid + 2, hi)
            elif (mid - 1) % 2 == 1:
                return helper(lo, mid - 2)
            return helper(mid + 1, hi)
        
        return helper(0, len(nums) - 1)
        
