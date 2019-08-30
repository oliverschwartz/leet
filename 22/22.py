class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(n):
            if n == 1:
                return ["()"]
            else: 
                seen = set()
                prev = recursive(n - 1)
                
                for s in prev:
                    seen.add("()" + s)
                    for index, c in enumerate(s):
                        if c == "(":
                            to_add = s[:index + 1] + "()" + s[index + 1:]
                            if to_add not in seen:
                                seen.add(to_add)
                
                return list(seen)
        
        return recursive(n)
