class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) < 2: return 0
    
        timePoints.sort()
        
        # Corner case: initialize a `champ` difference
        # to the difference between the first and last
        # elements in the sorted array (i.e. wrapping around)
        champ = self.endDiff(timePoints[0], timePoints[-1])
        
        # Walk along the adjacent pairs in the sorted array,
        # computing the difference between adjacent elements.
        i = 0
        j = 1
        while j < len(timePoints):
            diff = self.timeDiff(timePoints[i], timePoints[j])
            if diff < champ:
                champ = diff
            i += 1
            j += 1
        return champ
    
    # The difference between the first and last
    # time in the sorted array (we are doing 'wraparound')
    def endDiff(self, first, last):
        mins = int(first[-2:]) + 60 - int(last[-2:])
        hours = int(first[:2]) + 23 - int(last[:2])
        return hours * 60 + mins
    
    # The difference between two times
    def timeDiff(self, earlier, later):
        hours = int(later[:2]) - int(earlier[:2])
        mins = int(later[-2:]) - int(earlier[-2:])
        return hours * 60 + mins