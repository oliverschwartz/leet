class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        num = float(num)
        
        # Continue dividing `num` by 4 until it
        # is less than or equal to 1. If it is 
        # equal to 1, it is a power of 4. 
        while num > 1:
            if not float.is_integer(num): 
                return False
            num = num / 4
        if num == 1:
            return True
        return False