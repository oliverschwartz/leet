class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []: return 0
        
        # this dp arr tells us for i, j which are the
        # coords of the bottom right corner of a square with max side length
        # dp_arr[i][j]
        dp_arr = matrix
        
        # the key here is realizing that for m[][j] to be a square, 
        # then m[i - 1][j], m[i][j - 1] and m[i - 1][j - 1] must also be squares
        m, n, max_area = len(matrix), len(matrix[0]), 0
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    if dp_arr[i][j] != '0':
                        dp_arr[i][j] =  max(
                            min(
                                int(dp_arr[i - 1][j]),
                                int(dp_arr[i][j - 1]),
                                int(dp_arr[i - 1][j - 1])
                            ) + 1,
                            int(dp_arr[i][j])
                        )
                max_area = max(max_area, int(dp_arr[i][j]) * int(dp_arr[i][j]))
        return max_area