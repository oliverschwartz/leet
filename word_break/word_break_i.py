class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        # can you wordBreak s[idx => end]?
        memo = {}
        def recurseBreak(idx):
            if idx in memo:
                return memo[idx]
            
            # in this case, we know s[0:n] (the whole string)
            # can be wordBroken. So, return True here
            if idx == n:
                return True
            
            # otherwise, walk up the string.
            # Try a new split wherever possible
            end = idx
            while end < n:
                if s[idx : end + 1] in wordDict:
                    if recurseBreak(end + 1):
                        memo[idx] = True
                        return True
                end += 1
            memo[idx] = False
            return False
        
        return recurseBreak(0)