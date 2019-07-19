class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        # find eligible start targets
        min_gas = [max(cost[i] - gas[i], 0) for i in range(n)]
        start_targets = [idx for idx, n in enumerate(min_gas) if n == 0]
        if start_targets == []: return -1
        
        
        # max gas is an array containing the max gas we've seen at 
        # a given station
        # so if we arrive there with less, we can tap out immediately
        max_gas = [0 for i in range(n)]

        # trial and error on eligible targets
        for idx in start_targets:
            cur_gas = gas[idx] - cost[idx]
            pos = (idx + 1) % n
            while True:
                if cur_gas >= max_gas[pos]:
                    max_gas[pos] = max(max_gas[pos], cur_gas)
                    if pos == idx: return idx
                    cur_gas += (gas[pos] - cost[pos])
                    pos = (pos + 1) % n
                else: break
        return -1
  