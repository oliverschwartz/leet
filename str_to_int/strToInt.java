import java.lang.Math;

class Solution {
    public int myAtoi(String s) {
        
        // remove whitespace
        s = s.trim();
 
        if (s.isEmpty()) return 0;
        
        // check for + or - at beginning of string
        int displacement = 0;
        boolean negative = false;
        if (s.charAt(0) == '-') {
            negative = true;
            displacement++;
        }
        else if (s.charAt(0) == '+') displacement++;
        
        int sum = 0;
        for (int i = displacement; i < s.length(); i++) {
            char c = s.charAt(i);
            int j = Character.getNumericValue(c);
            
            // ignore non numeric characters after the number
            if (!Character.isDigit(c)) break;
            
            try { sum = Math.multiplyExact(sum, 10); }
            catch (ArithmeticException e) {
                if (negative) return Integer.MIN_VALUE;
                else return Integer.MAX_VALUE;
            }
            
            try { sum = Math.addExact(sum, j); }
            catch (ArithmeticException e) {
                if (negative) return Integer.MIN_VALUE;
                else return Integer.MAX_VALUE;
            }
        }
        
        if (negative) sum = -sum;
        return sum;
    }
}