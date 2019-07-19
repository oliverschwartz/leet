class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // check valid input
        assert k <= nums.length;
        
        // find sum of first k integers
        int sum = 0;
        for (int i = 0; i < k; i++)
            sum += nums[i];

        int maxSum = sum;
        
        // use a sliding window of length k
        for (int right = k; right < nums.length; right++) {
            sum += nums[right];
            sum -= nums[right - k];
            if (sum > maxSum) maxSum = sum;
        }
        
        return (double) maxSum / k;
    }
}