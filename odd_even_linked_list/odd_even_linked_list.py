# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        
        cur = head.next.next
        odd_root = ListNode(head.val)
        even_root = ListNode(head.next.val)
        odd_head = odd_root
        even_head = even_root
        count = 0

        while cur is not None:
            
            # odd node
            if count % 2 ==0:
                odd_head.next = ListNode(cur.val)
                odd_head = odd_head.next
             
            # even node
            else:
                even_head.next = ListNode(cur.val)
                even_head = even_head.next
                
            count += 1 
            cur = cur.next

        odd_head.next = even_root
        return odd_root
