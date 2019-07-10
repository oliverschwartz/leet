class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n == 1: return 1
        
        # sliding window!
        max_size = 1
        prev_cmp = None
        i, j = 0, 0
        while j < n - 1:
            j += 1
            
            # return early if we're not going to beat our best
            if n - i < max_size: break
            
            # if valid turbulent update max and previous comparison
            if (A[j] != A[j - 1] and
                (prev_cmp is None or prev_cmp != (A[j] > A[j - 1]))):
                max_size = max(max_size, j - i + 1)
                prev_cmp = A[j] > A[j - 1] 
                
            # if invalid because elements are equal, bring i all the way up to j
            # and set prev_cmp to None (it's like we're restarting from scratch)
            elif A[j] == A[j - 1]:
                i = j
                prev_cmp = None
                
            # otherwise just bring i up to j - 1
            else:
                i = j - 1
                prev_cmp = A[j] > A[j - 1] 
                
        return max_size
            
            