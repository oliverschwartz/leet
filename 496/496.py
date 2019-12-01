class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {}
        to_return = []
        l = len(nums2)
        
        for i, num in enumerate(nums2):
            indices[num] = i
        
        for num in nums1:
            index = indices[num]
            added = False
            
            for i in range(index + 1, l):
                if nums2[i] > num:
                    to_return.append(nums2[i])
                    added = True
                    break
            if not added:
                to_return.append(-1)
        
        return to_return
        
