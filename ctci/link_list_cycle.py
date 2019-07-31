# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""version using a hashtable O(n) time O(n) space"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        seen = set()
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
                head = head.next
        return False

"""version using two pointers O(n) time O(1) space"""     self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        
        fast = head.next
        slow = head
        
        while fast and fast.next and slow:
            if fast == slow: return True
            fast = fast.next.next
            slow = slow.next
            
        return False