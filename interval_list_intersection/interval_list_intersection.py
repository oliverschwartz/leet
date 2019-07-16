class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if A == [] or B == []: return []
        
        out = []
        n, m = len(A), len(B)
        i, j = 0, 0
        a_cur, b_cur = A[i], B[j]
        
        while i < n and j < m:
            if (A[i][0] <= B[j][1] and A[i][1] >= B[j][0]):
                out.append([
                    max(A[i][0], B[j][0]),
                    min(A[i][1], B[j][1])
                ])
                if A[i][1] < B[j][1]: i += 1
                else: j += 1
                
            elif A[i][0] > B[j][1]: j += 1
                
            elif B[j][0] > A[i][1]: i += 1
        return out