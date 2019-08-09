class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        count_s = {}
        for c in s:
            count_s[c] = count_s[c] + 1 if c in count_s else 1
            
        for c in t:
            if c not in count_s:
                return c
            else:
                count_s[c] -= 1
                if count_s[c] == 0:
                    del count_s[c]