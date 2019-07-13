class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        cands = sorted(candidates)

        def recurseSearch(cands, nums, target, ret):
            
            # base case
            if target == 0:
                ret.add(tuple(nums))
                return
            
            for idx, c in enumerate(cands):
                # once we hit something larger, no point search further
                if target - c < 0: break   
                else: recurseSearch(cands[idx+1:], nums + [c], target - c, ret)
        
        ret = set()
        recurseSearch(cands, [], target, ret)
        return [list(x) for x in ret]
                    
        s