class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        # we build a DP array where dp[i][j] gives either True or
        # False for whether s[i] to s[j] is a palindrome or not
        # we initialize all single digits to True
        n = len(s)
        pal = n
        dp = [[i == j for j in range (n)] for i in range(n)]
        
        # now, starting from back of string, check using two pointers
        # we keep moving i back while traversing j to the end
        i = n - 1
        while i >= 0:
            j = i
            while j < n:
                if s[i] == s[j]:
                    
                    # e.g, if aba is a palindrome, so is cabac
                    if i < n - 1 and j > 0 and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        pal += 1
                    
                    # case where we are dealing with two adjacent chars
                    elif j - i == 1:
                        dp[i][j] = True
                        pal += 1
                j += 1
            i -= 1

        return pal