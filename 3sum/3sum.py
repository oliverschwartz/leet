class Solution:  
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        
        # calculate length and sort
        n = len(nums)
        nums = sorted(nums)
        
        # traverse possible first elements of triples
        for i in range(n - 2):
            
            # the array is sorted, so once we're passed nums[i] > 0
            # we can stop looking (no chance it sums to 0)
            if nums[i] > 0: break
            
            # skip if we'd be looking at the same first element
            # as the previous iteration
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            # use sliding window, starting j just above i, and k just below end
            # we are basically checking for the second two elements of triples
            j = i + 1
            k = n - 1
            count = 0
            while j < k:
                
                # if total is too low, move j up
                if  nums[i] + nums[j] + nums[k] < 0: j += 1
                    
                # if total is too high, move k down
                elif  nums[i] + nums[j] + nums[k] > 0: k -= 1
                    
                # total is just right, add it to triples then skip duplicates by 
                # moving inwards on any equal numbers
                else:
                    triples.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    
                    # take one more step after we've walked in
                    j += 1
                    k -= 1
                                
        return triples
        