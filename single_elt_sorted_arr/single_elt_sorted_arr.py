class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # annoying edge case
        if n == 1: return nums[0]

        # binary search, using the fact that we know
        # to move left or right depending on whether a pair we are on
        # has odd-even indexes, or even-odd (the single element 'displaces'
        # elements to the right
        # 
        # for example
        #   [3,   3,   7,   7,   10,   11,   11]
        #   [0,   1,   2,   3,   4,    5,    6]
        #   even  odd  even odd  even  odd   even
        #   RIGHT      RIGHT   TARGET   LEFT
        
        l = 0
        r = n - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # condition where we've found the single number, including edge cases
            if (
                mid == 0 and nums[mid] != nums[mid + 1] or
                mid == n - 1 and nums[mid] != nums[mid - 1] or
                nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]
            ):
                return nums[mid]
            
            # case where we need to move right. In this case, for a pair of equal
            # elements, the left one is at an even index while the right one is at an
            # odd index. Note we could be sitting at either one
            elif (
                mid % 2 == 0 and nums[mid] == nums[mid + 1] or
                mid % 2 == 1 and nums[mid] != nums[mid + 1]
            ):
                l = mid + 1
                
            else:
                r = mid - 1
            
        return None
        