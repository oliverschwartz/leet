class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == []:
            return 0
        
        nr, nc = len(obstacleGrid), len(obstacleGrid[0])

        def get_nbors(x, y):
            for (a, b) in [(1, 0), (0, 1)]:
                if (
                    0 <= x + a <= nr - 1 and
                    0 <= y + b <= nc - 1 and
                    not obstacleGrid[x + a][y + b]
                ):
                   yield (x + a, y + b)
        
        memo = {}
        def helper(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            elif obstacleGrid[x][y]:
                return 0
            elif (x, y) == (nr - 1, nc - 1):
                return 1
            else:
                memo[(x, y)] = sum([helper(r, c) for (r, c) in get_nbors(x, y)])
                return memo[(x, y)]
        
        return helper(0, 0)