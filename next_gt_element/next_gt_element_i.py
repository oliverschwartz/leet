class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        gt = {}
        to_set = []
        for n in nums2:
            while to_set and to_set[-1] < n:
                gt[to_set.pop()] = n
            to_set.append(n)
        for idx, n in enumerate(nums1):
            nums1[idx] = gt[n] if n in gt else -1
        return nums1
        