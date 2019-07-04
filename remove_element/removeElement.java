class Solution {
    public int removeElement(int[] nums, int val) {
        int l = nums.length;
        
        // corner cases: empty and 1 element
        if (l == 0) return 0;
        else if (l == 1) {
            if (nums[0] == val) return 0;
            return 1;
        }
        
        // pointer to the stack of vals at end of array
        int end = l - 1;
        
        // move all val instances to end of array
        for (int i = 0; i < l; i++) {
            if (!(i < end)) break;
            
            if (nums[i] == val) {
                if (end > i) {
                    
                    // find next available position at the end
                    while (end > i && nums[end] == val)
                        end--;
                    if (!(end > i)) break;
                    
                    // swap elements
                    nums[i] = nums[end];
                    nums[end] = val;
                    end--;
                }
                else break;
            }
        }
        
        // corner case: end points at instance of val
        if (nums[end] == val) end--;
        return end + 1;
    }
}