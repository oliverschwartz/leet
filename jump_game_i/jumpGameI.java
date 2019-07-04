class Solution {
    public boolean canJump(int[] nums) {
        return canJump(nums, 0);
    }
    
    public boolean canJump(int[] nums, int start) {
        int end = nums.length - 1;

        if (start + nums[start] >= end) return true;
        
        boolean solved = false;
        while (nums[start] > 0 && !solved) {
            solved = canJump(nums, start + nums[start]);
            nums[start]--;
        }
        return solved;
    }
}
