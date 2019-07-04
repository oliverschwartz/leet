import java.lang.StringBuilder;

class Solution {
    public String convert(String s, int n) {
        if (n == 1) return s;
        
        StringBuilder sb = new StringBuilder();
        int len = s.length(); // length of input 
        int toTop = 0;        // number of positions from top of zig-zag
        int toBtm = 0;        // number of positions from bottom of zig-zag
        int toAdd = 0;        // index to add to get the next char
        int j = 0;
        boolean onDiag = false; // if we are on the diagonal in zig-zag
        
        // for each row
        for (int i = 0; i < n; i++) {
            
            // if top or bottom row, chars are 2(n-1) apart
            if (i == 0 || i == n - 1)
                for (j = i; j < len; j += 2*(n - 1))
                    sb.append(s.charAt(j));
            
            // iterate through the zig-zag, building the string
            else {
                toTop = i;
                toBtm = (n-1) - i;
                if (onDiag) toAdd = 2 * toTop;
                else toAdd = 2 * toBtm;
                
                for (j = i; j < len; ) {
                    int oldJ = j;
                    j += toAdd;
                    sb.append(s.charAt(oldJ));
                    if (onDiag) toAdd = 2 * toBtm;
                    else toAdd = 2 * toTop;
                    onDiag = !onDiag;
                }
                onDiag = false;
            }
        }
        
        return sb.toString();
    }
}
