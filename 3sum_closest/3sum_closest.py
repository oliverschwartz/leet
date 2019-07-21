class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        n = len(nums)
        dist = float('inf')
        
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                # update min dist
                if abs(s - target) < abs(dist): dist = s - target
                    
                # found optimal solution
                if s == target: return target
                
                # need to increase sum
                elif s < target: j += 1
                    
                # need to decrease sum
                elif s > target: k -= 1
        
        return dist + target