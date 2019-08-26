# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMid(first):
            slow = first
            fast = first
            prevSlow = first
            
            while fast and fast.next:
                fast = fast.next.next
                prevSlow = slow
                slow = slow.next
                
            prevSlow.next = None
            return slow
        
        def createTree(first):
            if not first:
                return None
            mid = getMid(first)
            print(mid.val)
            newNode = TreeNode(mid.val)
            newNode.right = createTree(mid.next)
            if mid != first:
                newNode.left = createTree(first)
            else:
                newNode.left = None
            return newNode
        
        return createTree(head)
        
