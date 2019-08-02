# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # Resevoir sampling: at each point, update the `current`
        # value with probability 1 / i (where we have seen i nodes)
        i = 0
        head = self.head
        current = head.val
        
        while head:
            i += 1
            rand = random.random()
            if rand < 1 / i:
                current = head.val
            head = head.next
            
        return current
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()