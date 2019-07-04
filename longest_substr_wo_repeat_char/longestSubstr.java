class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        String tmp = "";
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (tmp.indexOf(c) == -1) {
                tmp += c;
                if (tmp.length() > maxLen)
                    maxLen = tmp.length();
            }
            else {
                tmp += c;
                int firstIndexOf = tmp.indexOf(c);
                tmp = tmp.substring(firstIndexOf + 1);
            }
        }
        return maxLen;
    }
}