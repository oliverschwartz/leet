class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def get_nbors(x, y):
            for (a, b) in [(1, 0), (0, 1)]:
                if 0 <= x + a <= n - 1 and 0 <= y + b <= m - 1:
                   yield (x + a, y + b)
        
        memo = {}
        def helper(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            elif (x, y) == (n - 1, m - 1):
                return 1
            else:
                memo[(x, y)] = sum([helper(r, c) for (r, c) in get_nbors(x, y)])
                return memo[(x, y)]
        
        return helper(0, 0)