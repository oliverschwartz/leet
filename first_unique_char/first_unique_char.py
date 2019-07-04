class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        n = len(s)
        non_repeating = {}
        seen = set()

        for i in range(n - 1, -1, -1):
            if s[i] not in seen:
                non_repeating[s[i]] = i
                seen.add(s[i])
            elif s[i] in non_repeating:
                del non_repeating[s[i]]
        
        return -1 if non_repeating == {} else min(non_repeating.values())