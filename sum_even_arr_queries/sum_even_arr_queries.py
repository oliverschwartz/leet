class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        original = sum([x for x in A if x % 2 == 0])

        # perform queries and figure out ans from previous
        ans = [original]
        for idx, q in enumerate(queries):
            old = A[q[1]]
            A[q[1]] += q[0]
            new = A[q[1]]

            # conditions depend on whether we went from even/odd => even/odd  
            if old % 2 == 0 and new % 2 == 0: ans.append(ans[idx] + new - old)
            elif old % 2 == 0: ans.append(ans[idx] - old)
            elif new % 2 == 0: ans.append(ans[idx] + new)
            else: ans.append(ans[idx]) 

        return ans[1:]