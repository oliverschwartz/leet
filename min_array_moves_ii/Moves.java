import java.util.Arrays;
import java.lang.Math;

class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        
        int median = nums[nums.length / 2];
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += Math.abs(median - nums[i]);
        }
        
        return sum;
    }
}