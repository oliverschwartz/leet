class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        n = len(A)

        # run through to find which number will actually fill a row
        row_fill_set = set([A[0], B[0]])
        A_counts, B_counts = {}, {}
        for i in range(n):
            A_counts[A[i]] = A_counts[A[i]] + 1 if A[i] in A_counts else 1
            B_counts[B[i]] = B_counts[B[i]] + 1 if B[i] in B_counts else 1
            row_fill_set = row_fill_set.intersection(set([A[i], B[i]]))
            if not row_fill_set: return -1
        
        # see whether it will swap faster if we fill A, or B
        target = row_fill_set.pop()
        return min(n - A_counts.get(target, 0), n - B_counts.get(target, 0))