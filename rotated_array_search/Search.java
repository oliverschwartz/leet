class Solution {
    public int search(int[] nums, int target) {
        if (nums == null) return -1;
        
        return bsearch(nums, 0, nums.length, target);
    }
    
    // Modified binary search: recurse on both the left 
    // and right sub-halves.
    private int bsearch(int[] nums, int lo, int hi, int target) {
        if (hi <= lo) return -1;
        
        int mid = (hi + lo) / 2;
        
        if (nums[mid] == target) 
            return mid;
        int left = bsearch(nums, lo, mid, target);
        int right = bsearch(nums, mid + 1, hi, target);
        if (left != -1) return left;
        else if (right != -1) return right;
        return -1;
    }
}