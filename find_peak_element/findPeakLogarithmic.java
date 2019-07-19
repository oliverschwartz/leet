class Solution {
    public int findPeakElement(int[] nums) {
        // corner cases: length 1 and peak on ends
        int l = nums.length;
        if (l == 1) return 0;
        else if (nums[0] > nums[1]) return 0;
        else if (nums[l - 1] > nums[l - 2]) return l - 1;
        
        
        return findPeak(nums, 0, l);
    }
    
    private int findPeak(int[] nums, int lo, int hi) {
        if (hi < lo) throw new IllegalArgumentException();
        
        int mid = (hi + lo) / 2;
        if (nums[mid] > nums[mid - 1]) {
            if (nums[mid] > nums[mid + 1]) return mid;
            else return findPeak(nums, mid + 1, hi);   
        }
        else return findPeak(nums, lo, mid);
    }
}