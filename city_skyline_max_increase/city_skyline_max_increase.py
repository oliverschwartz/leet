class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # grid: m rows X n cols
        m = len(grid)   
        n = len(grid[0])
        if m == 0 or n == 0: return 0
        
        max_rows = []
        max_cols = []
        
        # find max of each row
        for row in grid:
            champ = 0
            for h in row:
                if h > champ: champ = h
            max_rows.append(champ)

        # find max of each col
        for j in range(n):
            champ = 0
            for i in range(m):
                if grid[i][j] > champ: champ = grid[i][j]
            max_cols.append(champ)
            
        print(max_cols)
        print(max_rows)
            
        # iterate over grid, keeping a cumulative sum
        # for each building, it can grow to min(maxOfThatRow, maxOfThatCol)
        growth = 0
        for i in range(m):
            for j in range(n): 
                growth += min(max_rows[i], max_cols[j]) - grid[i][j] 
                
        return growth
                
        