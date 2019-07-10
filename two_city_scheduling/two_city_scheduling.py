class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n, total, num_A, num_B = len(costs) / 2, 0, 0, 0
        
        # sort by descending cost difference
        sorted_costs = sorted(costs, key=lambda x: -abs(x[0] - x[1]))
        for c in sorted_costs:
            
            # overflows
            if num_B == n:
                total += c[0]
                num_A += 1
            elif num_A == n:
                total += c[1]
                num_B += 1
                
            # otherwise
            elif c[0] < c[1]:
                total += c[0]
                num_A += 1
            elif c[1] < c[0]:
                total += c[1]
                num_B += 1
            
        return total