class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        seen = set()

        def dfs(grid, i, j):
            stack = [(i, j)]

            while stack:
                coors = stack.pop()
                seen.add(coors)
                nbors = get_nbors(coors[0], coors[1])
                for n in nbors:
                    if grid[coors[0]][coors[1]] == "1" and n not in seen:
                        stack.append(n)

        def get_nbors(i, j):
            for (a, b) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= a + i <= nr - 1 and 0 <= b + j <= nc - 1:
                    yield (a + i, b + j)
        
        islands = 0
        
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(grid, i, j)
                    islands += 1
        return islands
        
        
            