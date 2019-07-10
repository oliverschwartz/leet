class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        NUM_CHARS = 26
        
        # represent words as tuples of 26 values, corresponding to character
        # count. For example, 'at' would be (1, 0, 0, ..., 1, ...)
        # words are anagrams if they have the same tuple
        #
        # ans is a map from tuple count to index list
        #
        ans = {}
        for idx, s in enumerate(strs):
            t_rep = [0 for x in range(NUM_CHARS)]
            for c in s: t_rep[ord(c) - ord('a')] += 1
            t_rep_tuple = tuple(t_rep)     # tuples are hashable
            if t_rep_tuple in ans: ans[t_rep_tuple].append(idx)
            else: ans[t_rep_tuple] = [idx]
        return [[strs[i] for i in idx_list] for idx_list in ans.values()]
       
        