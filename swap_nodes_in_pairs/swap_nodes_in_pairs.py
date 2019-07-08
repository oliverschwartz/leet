# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current is not None:
            if current.next is None: break # odd number of nodes
            elif current == head:
                head = head.next
            else: prev.next = current.next 
            
            # swap pair of nodes
            tmp = current.next.next
            current.next.next = current
            current.next = tmp
            prev = current
            current = tmp
        return head
        