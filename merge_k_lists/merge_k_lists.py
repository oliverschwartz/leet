# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        """Without inbuilt sort
        
        O(nK) where K is # lists, n is average length"""
        lists = [x for x in lists if x]
        if len(lists) == 0: return None
        
        head = ListNode(None)
        cur = head
        counter = 0
        while lists:
            val = float('inf')
            node = None
            min_idx = None
            for idx, p in enumerate(lists):
                if p.val < val: val, node, min_idx = p.val, p, idx
            cur.next = node
            cur = cur.next
            lists[min_idx] = node.next
            lists = [x for x in lists if x]
        return head.next

    def mergeKListsCheating(self, lists: List[ListNode]) -> ListNode:  

        """With inbuilt sort
        
        O((nK) log (nK)) where K is # lists, n is average length"""

        vals = []
        for l in lists:
            while l:
                vals.append(l)
                l = l.next

        vals = sorted(vals, key=lambda x: x.val)
        n = len(vals)
        for idx, v in enumerate(vals):
            if idx < n - 1: v.next = vals[idx + 1]
            else: v.next = None
        return vals[0] if len(vals) > 0 else None