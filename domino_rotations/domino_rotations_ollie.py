class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        l = len(A)
        if l == 1: return 0 # edge case
        
        # count frequencies
        freq_A = {}
        freq_B = {}
        for i in range(l):
            if freq_A.__contains__(A[i]): freq_A[A[i]] += 1
            else: freq_A[A[i]] = 1
            if freq_B.__contains__(B[i]): freq_B[B[i]] += 1
            else: freq_B[B[i]] = 1
               
        # see if any numbers satisfy the condition
        champ = -1
        for i in range(1, 7, 1):
            if freq_A.get(i, 0) + freq_B.get(i, 0) >= l:
                valid = True
                for j in range(l):
                    if A[j] != i and B[j] != i: valid = False
                if valid: champ = l - max(freq_A[i], freq_B[i])
        return champ