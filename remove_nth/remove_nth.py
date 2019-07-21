# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next: return None
        
        # fast is the lead element. remove is the element to remove
        # prev is the element before remove
        fast = head
        remove = head
        prev = None
        
        for i in range(n - 1): fast = fast.next
        
        # we must be ditching the first element
        if not fast.next: return head.next
        
        # otherwise, create prev -> remove -> ... -> fast, then point
        # prev.next to remove.next (cutting out remove)
        while fast.next:
            prev = remove
            remove = remove.next
            fast = fast.next    
        prev.next = remove.next
        return head
