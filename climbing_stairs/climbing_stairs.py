class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        # dynamic programming approach:
        # build a map of number of stairs: possible ways
        d = {}
        for i in range(n):
            if i == 0: d[0] = 0
            elif i == 1: d[1] = 1
            elif i == 2: d[2] = 2
            else: d[i] = d[i-1] + d[i-2]
                
        return d[n-1] + d[n-2]