class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # annoying edge case
        if numRows == 1:
            return s
        
        rows = [[] for _i in range(numRows)]
        
        # how many chars there are in each zigzag grouping
        zigZagSize = 2 * numRows - 2

        for idx, c in enumerate(s):
            
            # we're in the 'zig' (vertical) of a group
            # correct row is just the mod of the index
            if idx % zigZagSize <= (numRows - 1):
                rows[idx % zigZagSize].append(c)
              
            # we're in the 'zag' (diagonal) of a group
            # correct row is the zigZagSize minus the mod of the index
            else:
                rows[zigZagSize - (idx % zigZagSize)].append(c)
            
            
        return ''.join([''.join(x) for x in rows])
