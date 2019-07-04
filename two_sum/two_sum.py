class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # speed things up by storing a mapping of
        # number => index for fast lookups
        hash_table = {}
        
        # traverse the numbers list, inserting into hashtable
        # at each step if we find the complement (target - current_number)
        # already in the hashtable we can return.
        # this lets us get O(n) time and O(n) space
        for (idx, n) in enumerate(nums):
            if (target - n) in hash_table:
                return [hash_table[target - n], idx]
            else:
                hash_table[n] = idx