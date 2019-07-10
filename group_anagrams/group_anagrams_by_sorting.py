class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # build dict mapping sorted s => list of indices
        ans = {}
        for idx, s in enumerate(strs):
            st = ''.join(sorted(s))
            if st in ans: ans[st].append(idx)
            else: ans[st] = [idx]
        return [[strs[i] for i in idx_lst] for idx_lst in ans.values()]
