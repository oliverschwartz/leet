class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        cands = sorted(candidates, reverse=True)
        n = len(cands)
        self.combos = set()
        
        def recurseCombo(idx, target, sol):
            orig = sol
            if idx >= n: return
            else:
                cur = cands[idx]
                sol = sol + (cands[idx],)
                while cur < target:
                    recurseCombo(idx + 1, target - cur, sol)
                    cur += cands[idx]
                    sol = sol + (cands[idx],)
                if cur == target: 
                    self.combos.add(sol)
                recurseCombo(idx + 1, target, orig)
                    
        recurseCombo(0, target, ())
                    
        return [list(combo) for combo in self.combos]

