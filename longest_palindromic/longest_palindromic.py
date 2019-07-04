class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 2D matrix which for i, j indices in s
        # tells us whether dp_store[i][j] is a palindrome or not
        #
        # we initialize it so that for i in len(s), dp[i][i] = True
        # since all 1-char strings are palindromes
        #
        n = len(s)
        longest = ''
        dp_store = [[x == i for x in range(n)] for i in range(n)]
        
        # we want to fill in the dp_store matrix to the upper right of the 
        # diagonal. This means e.g. for 'abcde', we would iterate
        # i=4 j=4; i=3 j=3; i=3 j=4; i=2 j=2, i=2 j=3, i=2 j=4; etc
        #
        # basically moving i right to left, and moving j from i to len(s)
        #
        for i in range(n - 1, -1, -1):       # i goes from n -> 0
            for j in range(i, n):            # j goes from i -> n
                if s[i] == s[j]:
                    
                    # it's a palindrome if the dp entry diagonally left and down
                    # of it is also a palindrome - e.g. 'abba' is a palindrome if 'bb' is one
                    # but must also check this won't go outside the boundaries
                    dp_store[i][j] = dp_store[i][j] or (i + 1 < n and dp_store[i + 1][j - 1])
                    
                    # it's also a palindrome if it's length 2 
                    if j - i == 1:
                        dp_store[i][j] = True
                    
                    # update longest if we found a new one
                    if (j - i) + 1 > len(longest) and dp_store[i][j]:
                        longest = s[i:j + 1]
                    
        return longest