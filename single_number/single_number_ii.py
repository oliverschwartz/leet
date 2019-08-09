class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seen_once = 0
        seen_twice = 0
        
        for n in nums:
            
            # ^ n done once will put n into seen_once, if n not in seen_twice
            # ^ n twice will remove it from seen_once, and put it into seen_twice
            seen_once = (seen_once ^ n) & ~seen_twice
            seen_twice = (seen_twice ^ n) & ~seen_once

        return seen_once