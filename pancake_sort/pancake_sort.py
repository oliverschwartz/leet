class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        flips = []
        
        """Our strategy is to iterate elements, finding the largest 
        element in A[0: n - i] each time. We then flip the index where that element
        is, so it goes to the beginning.
        
        Then, we flip the whole array minus the current
        index, to put it to the end (minus the number of spots we are along in the iteration)"""
        
        for i in range(n):
            
            # find the max element and its index
            largest = -1
            largest_idx = -1
            for idx, val in enumerate(A[0:n-i]):
                if val > largest:
                    largest_idx = idx
                    largest = val
            
            # flip the largest element to beginning, then flip it to the end
            r = A[0:largest_idx+1]
            r.reverse()
            A = r + A[largest_idx+1:n]
            r = A[0:n-i]
            r.reverse()
            A = r + A[n-i:n]
            
            # update flips
            flips.append(largest_idx + 1)    
            flips.append(n-i)
            
        return flips