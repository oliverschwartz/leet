# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        fast = head
        slow = head
        seen = {head.val}
        while fast:
            while fast and fast.val in seen:
                fast = fast.next
            if fast: seen.add(fast.val)
            slow.next = fast
            slow = slow.next
        return head