# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        
        slow = head
        fast = head
        stack = []

        # traverse first half of list, push to stack
        odd = True
        while fast.next is not None:
            stack.append(slow.val)
            slow = slow.next
            if fast.next.next is None:
                fast = fast.next
                odd = False
            else: fast = fast.next.next
        
        # skip middle element if it's an odd list
        if odd: slow = slow.next
    
        while slow is not None:
            if stack.pop() != slow.val: return False
            slow = slow.next
        return True
            