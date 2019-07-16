class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            
            # in a sorted subarray, normal binary search
            if nums[l] <= nums[mid] <= nums[r]:
                if nums[mid] > target: r = mid - 1
                else:  l = mid + 1
            
            # spanning pivot, mid in left part
            elif nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                if nums[l] > target or nums[mid] < target: l = mid + 1
                else: r = mid - 1
            
            # spanning pivot, mid in right part
            else:
                if nums[r] < target or nums[mid] > target: r = mid - 1
                else: l = mid + 1
            
        return -1