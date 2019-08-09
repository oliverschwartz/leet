class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)

        min_rights = [None for i in range(n)]
        for i in range(n):
            if i == 0:
                min_rights[n - i - 1] = A[n - i - 1]
            else:
                min_rights[n - i - 1] = min(A[n - i - 1], min_rights[n - i])
        
        max_left = A[0]
        idx = 0
        while max_left > min_rights[idx + 1]:
            idx += 1
            max_left = max(max_left, A[idx])
        return idx + 1