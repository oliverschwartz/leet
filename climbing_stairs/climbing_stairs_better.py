class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        # dynamic programming approach:
        # build a map of number of stairs: possible ways
        prev0 = 1
        prev1 = 2
        s = 2
        for i in range(2, n):
            s = prev0 + prev1
            prev0 = prev1
            prev1 = s
                
        return s
