class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        out = []
        popped_idx = 0
        for l in pushed:
            stack.append(l)
            while stack and stack[-1] == popped[popped_idx]:
                out.append(stack.pop())
                popped_idx += 1
        
        return out == popped