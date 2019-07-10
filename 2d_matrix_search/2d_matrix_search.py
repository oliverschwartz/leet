class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        return self.bsearch(matrix, len(matrix) * len(matrix[0]) - 1, 0, target)
        
    def bsearch(self, matrix, hi, lo, target):
        if not hi >= lo: return False
        
        mid = (hi + lo) // 2
        coors = self.to_2d(mid, len(matrix[0]))
        
        if matrix[coors[1]][coors[0]] == target: return True
        elif matrix[coors[1]][coors[0]] < target: return self.bsearch(matrix, hi, mid+1, target)
        else: return self.bsearch(matrix, mid - 1, lo, target)
    
    def to_2d(self, index, cols):
        return (int(index % cols), int(index // cols))
        