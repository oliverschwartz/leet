class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []: return intervals
        
        # sort by left values, then just run through, 
        # merging anything adjacent that we can
        intervals = sorted(intervals)
        ret = []
        prev = None
        tmp = intervals[0]
        for i in intervals:
            if not prev:
                prev = i
                continue
            elif i[0] > prev[1]:
                ret.append(prev)
                prev = i
                continue
            elif i[0] <= prev[1]:
                prev = [prev[0], max(i[1], prev[1])]
        ret.append(prev)
        return ret
        