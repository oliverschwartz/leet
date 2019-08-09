class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # at the end of this,
        # n1_xor_n2 will be the xor of our two numbers
        # since n ^ n = 0 and all the pairs will cancel
        n1_xor_n2 = 0
        for n in nums:
            n1_xor_n2 ^= n
            
        # find the last bit that's different between the two numbers
        # - this will just be the last set bit of n1_xor_n2 (we
        # can that witht the little trick below)
        #
        # then, do the same thing as above, but only consider
        # numbers with a bit at this point, using a condition
        #
        # once again, all pairs will cancel, but this time,
        # only one of the numbers will be left in our accumulator
        # variable due to the mask
        n1 = 0
        last_different_bit = n1_xor_n2 & -n1_xor_n2
        for n in nums:
            if last_different_bit & n:
                n1 ^= n
        
        return [n1, n1_xor_n2 ^ n1]
 