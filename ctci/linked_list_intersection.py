# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        curA = headA
        curB = headB
        sizeA = 0
        sizeB = 0
        while curA:
            curA = curA.next
            sizeA += 1
        while curB:
            curB = curB.next
            sizeB += 1
        
        while sizeA > sizeB:
            headA = headA.next
            sizeA -= 1
        while sizeB > sizeA:
            headB = headB.next
            sizeB -= 1
            
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
            
        return None