class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []: return [newInterval]
        
        # binary search, with cmp = < | >, 
        # such that if val doesn't exist, the closest 
        # val satisfying (val cmp target) will be returned
        def cmpBinarySearch(arr, val, val_idx, cmp):
            n = len(arr)
            l, r = 0, n - 1
            best = None
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][val_idx] == val: return mid
                elif val < arr[mid][val_idx]:
                    if cmp == '<': best = mid
                    r = mid - 1
                elif val > arr[mid][val_idx]:
                    if cmp == '>': best = mid
                    l = mid + 1
            return best
        
        # find smallest END value such that newInterval[0] <= END
        # using binary search
        end_idx = cmpBinarySearch(intervals, newInterval[0], 1, '<')
                
        # find largest START value such that newInterval[1] >= START
        # using binary search
        start_idx = cmpBinarySearch(intervals, newInterval[1], 0, '>')
        
        if end_idx is None:
            intervals.append(newInterval)
        elif start_idx is None:
            intervals = [newInterval] + intervals
        
        # update interval in place
        elif end_idx == start_idx:
            intervals[end_idx][0] = min(newInterval[0], intervals[end_idx][0])
            intervals[end_idx][1] = max(newInterval[1], intervals[end_idx][1])
            
        # insert interval into list
        elif start_idx < end_idx:
            intervals = intervals[:end_idx] + [newInterval] + intervals[start_idx+1:]
        
        # merge all intervals from end_idx to start_idx
        else:
            start = min(newInterval[0], intervals[end_idx][0])
            end = max(newInterval[1], intervals[start_idx][1])
            intervals = intervals[:end_idx] + [[start, end]] + intervals[start_idx+1:]

        return intervals
        
    
                    
                