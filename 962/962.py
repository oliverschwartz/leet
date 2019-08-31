 class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        indices = sorted(range(len(A)), key=lambda x: A[x])
        smallest = indices[0]
        champ = -float("inf")
        
        for i, index in enumerate(indices):
            if i == 0:
                continue
            if index < smallest:
                smallest = index
            if index - smallest > champ:
                champ = index - smallest
            
        if champ == -float("inf"):
            champ = 0
        return champ
