class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # annoying edge case
        if len(s) == 0:
            return 0
        
        # track two indices in the string, i and j
        # increment i when there's no duplication, otherwise increment j
        i = 0
        j = 0
        
        # this is our return value, a continually updated record of 
        # the longest substring
        v = 1
        
        # track a memoized record of members of the substring
        # so we can compare as we go and check validity
        contents = set(s[i])
        
        # once we hit the end of the string it's time to stop
        while(i < len(s) - 1):
            
            # move front of substr
            i += 1
            
            # need to move the back of substr along if we violated the constraint
            # if j moves up to i then also stop this process
            while (s[i] in contents and j != i):
                contents.remove(s[j])
                j += 1
                
            # add to previous and update max
            contents.add(s[i])
            v = max(v, i - j + 1)

        return v