# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""Recursive solution"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        
        def recurseReverseList(head):
            if not head.next: return head
            else:
                out = recurseReverseList(head.next)
                out.next = head
                head.next = None
                return head
        
        cur = head
        while cur.next is not None: cur = cur.next
        recurseReverseList(head)
        return cur


"""Iterative, form entirely new list"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
       
        new_head = ListNode(stack.pop())
        cur = new_head
        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next
        return new_head
            