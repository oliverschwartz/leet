class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        n = len(s)
        self.ans = set()
        
        # can you wordBreak s[idx => end]?
        memo = {}
        def recurseBreak(idx, cur):
            if (idx, cur) in memo:
                return
            memo[(idx, cur)] = True
            
            # in this case, we know s[0:n] (the whole string)
            # can be wordBroken. So, add solution here
            if idx == n:
                self.ans.add(cur)
            
            # otherwise, walk up the string.
            # Try a new split wherever possible
            end = idx
            while end < n:
                if s[idx : end + 1] in wordDict:
                    new = cur + ' ' + s[idx : end + 1] if cur != '' else s[idx : end + 1]
                    recurseBreak(end + 1, new)
                end += 1
        
        recurseBreak(0, '')
        return [x for x in self.ans]