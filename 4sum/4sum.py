class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # we sum up all the pairs
        # then look if we have any pairs of sums s1, -s2 + target
        # given s1 + s2 = target
        n = len(nums)
        sums = {}
        for i in range(n):
            for j in range(i, n):
                s = nums[i] + nums[j]
                if s in sums: sums[s].append((i, j))
                else: sums[s] = [(i, j)]

        fours = set()
        sums_seen = set()
        for s in sums:
            if s in sums_seen: continue
            elif -s + target in sums:
                for (i1, j1) in sums[s]:
                    for(i2, j2) in sums[-s + target]:
                        four = tuple(sorted([nums[i1], nums[j1], nums[i2], nums[j2]]))
                        if len(set([i1, j1, i2, j2])) == 4 and four not in fours:
                            fours.add(four)
            sums_seen.add(s)

        return [list(x) for x in fours]
                
        