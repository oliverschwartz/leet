class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k < 1: return
        
        self.combos = []
        
        
        def recurseComboSum(idx, sol, remaining, target):
            if remaining == 0 and target == 0:
                self.combos.append(list(sol))
                return
            elif target < 0: return
            elif remaining == 0: return
            else:
                for j in range(idx, 10):
                    if j not in sol:
                        recurseComboSum(j + 1, sol + (j,), remaining - 1, target - j)
                
        recurseComboSum(1, (), k, n)
        return self.combos