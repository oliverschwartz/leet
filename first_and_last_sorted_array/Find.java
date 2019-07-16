class Solution {
    /*
        Implementation: binary search. 
        
        - To find the left-most index, first search for the target.
        Then, repeatedly binary search the subarray to the left of the target,
        until no more `target`s are found.
        
        - The implementation for the right-most is identical.
    */
    public int[] searchRange(int[] nums, int target) {
        // corner cases
        if (nums.length == 0) return new int[]{-1, -1};
        if (nums.length == 1) {
            if (nums[0] == target) return new int[]{0, 0};
            else return new int[]{-1, -1};
        }
        
        // for clarity
        int hi = nums.length - 1;
        int lo = 0;
        
        // find the first position
        int leftIndex = bsearch(nums, target, hi, lo);
        int prevLeft = leftIndex;
        while (leftIndex != -1) {
            prevLeft = leftIndex;   
            leftIndex = bsearch(nums, target, leftIndex - 1, lo);
        }
        
        // find the last position
        int rightIndex = bsearch(nums, target, hi, lo);
        int prevRight = rightIndex;
        while (rightIndex != -1) {
            prevRight = rightIndex;   
            rightIndex = bsearch(nums, target, hi, rightIndex + 1);
        }
        
        return new int[]{prevLeft, prevRight};
    }
    
    // recursive binary search function
    private int bsearch(int[] nums, int target, int hi, int lo) {
        if (hi < lo) return -1;
        int mid = (hi + lo) / 2;
        
        if (nums[mid] == target) return mid;
        else if (nums[mid] > target) return bsearch(nums, target, mid - 1, lo);
        else return bsearch(nums, target, hi, mid + 1);
    }
}
