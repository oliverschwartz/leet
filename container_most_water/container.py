class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # track two indices, start from ends of the array
        i = 0
        j = len(height) - 1
        area = 0
        
        # walk inwards from ends until we meet
        # we choose which direction to walk in based on which of the 
        # two currently selected heights is smaller
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
            
        return area