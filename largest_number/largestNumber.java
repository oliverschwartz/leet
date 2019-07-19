import java.lang.StringBuilder;
import java.util.Arrays;

class Solution {
    private class CustomComparator implements Comparator<String> {
        @Override
        public int compare(String a, String b) {
            String order1 = a + b;
            String order2 = b + a;
            return order2.compareTo(order1);
        }
    }
    
    public String largestNumber(int[] nums) {
        CustomComparator comp = new CustomComparator();
        
        String[] stringArr = new String[nums.length];
        for (int i = 0; i < nums.length; i++)
            stringArr[i] = Integer.toString(nums[i]);
        
        Arrays.sort(stringArr, comp);
        if (stringArr[0].equals("0")) return "0";
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < stringArr.length; i++)
            sb.append(stringArr[i]);
        
        return sb.toString();
    }
}
