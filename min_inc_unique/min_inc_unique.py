class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        A = sorted(A)
        moves = 0
        for idx, n in enumerate(A):
            if idx > 0 and n <= A[idx - 1]:
                A[idx] = A[idx - 1] + 1
                moves += A[idx] - n
        return moves