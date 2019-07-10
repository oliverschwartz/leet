class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        matches = []
        
        for query in queries: 
            q = 0; p = 0
            while q < len(query):
                if not p < len(pattern):
                    if query[q].islower(): q += 1
                    else: break
                elif query[q].isupper() and pattern[p].isupper():
                    if query[q] == pattern[p]: 
                        q += 1
                        p += 1
                    else: break
                elif query[q].isupper() and pattern[p].islower(): break
                elif query[q].islower() and pattern[p].isupper(): q += 1
                elif query[q] == pattern[p]: 
                    q += 1
                    p += 1
                else: q += 1
            if q == len(query) and p == len(pattern):
                matches.append(True)
            else: matches.append(False)

        return matches