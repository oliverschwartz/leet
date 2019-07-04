import java.lang.Math;

class Solution {
    public int maxArea(int[] height) {
        // maintain pointers
        int right = height.length - 1;
        int left  = 0;
        
        int champion = 0;
        int area = 0;        
        
        // move pointers inwards until they meet
        while (left < right) {
            area = Math.min(height[left], height[right]) * (right - left);
            if (area > champion) champion = area;
            
            // move the pointer with smaller height, inwards
            if (height[left] > height[right]) right--;
            else left++;
        }
        
        return champion;    
    }
}
