class Solution {
    public int[] plusOne(int[] digits) {
        boolean carry = true;
        int i = digits.length - 1;
        
        while (carry && i >= 0) {
            if (digits[i] < 9) {
                carry = false;
                digits[i]++;
            }
            else {
                digits[i] = 0;
            }
            i--;
        }
        
        // if the number was all 9s
        if (digits[0] == 0) {
            int[] tmp = new int[digits.length+1];
            tmp[0] = 1;
            return tmp;
        }
        
        return digits;
    }
}