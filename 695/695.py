class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        seen = set()

        def dfs(grid, i, j):
            size = 0
            stack = [(i, j)]

            while stack:
                coors = stack.pop()
                if coors not in seen:
                    size += 1
                seen.add(coors)
                nbors = get_nbors(coors[0], coors[1])
                for n in nbors:
                    if grid[n[0]][n[1]] == 1 and n not in seen:
                        stack.append(n)
            return size

        def get_nbors(i, j):
            for (a, b) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= a + i <= nr - 1 and 0 <= b + j <= nc - 1:
                    yield (a + i, b + j)
        
        max_area = 0        
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1 and (i, j) not in seen:
                    area = dfs(grid, i, j)
                    if area > max_area:
                        max_area = area
        return max_area
        
        
            