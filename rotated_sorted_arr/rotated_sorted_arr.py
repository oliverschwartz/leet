class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        pivot_idx = None
        for idx, num in enumerate(nums):
            if idx > 0 and num < nums[idx - 1]:
                nums = nums[idx : n] + nums[0 : idx]
                pivot_idx = idx
                break
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return (mid + pivot_idx) % n if pivot_idx else mid
        return -1