"""Note - similar to the max rain water problem"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <=1: return 0

        # use sliding window and walk inwards from ends
        i, j = 0, n - 1
        left_wall, right_wall = height[i], height[j]
        trapped = 0
        while i < j:
            
            # if right wall is or equal taller, walk the left wall in
            # otherwise walk the right wall in
            if height[i] <= height[j]:
                if height[i] > left_wall: left_wall = height[i]
                else: trapped += left_wall - height[i]
                i += 1
            
            else:
                if height[j] > right_wall: right_wall = height[j]
                else: trapped += right_wall - height[j]
                j -= 1
                
        return trapped
                    