# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # return value and an a current value we use
        # to traverse
        ret = ListNode(0)
        cur = ret
        
        # keep going while we have something to add
        while(l1 or l2):
            
            # sum the current value (0 or 1 if a carry) and l1 and/or l2 
            # if they exist, and set current value to mod 10 of that
            s = cur.val + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.val = s % 10

            # next node starts on 1 if we carry
            if s >= 10:
                cur.next = ListNode(1)
                
            # return if we can't track any further
            if (not (l1 and l1.next) and not (l2 and l2.next)):
                return ret
            
            # otherwise increment as appropriate for l1, l2, cur
            else:
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
                cur.next = cur.next or ListNode(0)
                cur = cur.next