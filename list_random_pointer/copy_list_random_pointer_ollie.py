"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None
        
        # Map nodes from original list to 
        # their corresponding nodes in copied list.
        copy_head = Node(head.val, None, None)
        mapping = { head: copy_head }
        
        if head.random:
            if not mapping.__contains__(head.random):
                copy_head.random = Node(head.random.val, None, None)
                mapping[head.random] = copy_head.random
            else: copy_head.random = mapping[head.random]
        else: copy_head.random = None

        prev = copy_head
        head = head.next
        
        # One pass approach: iterate over the list, 
        # checking whether we have seen nodes before.
        while head is not None:
            if mapping.__contains__(head): current = mapping[head]
            else:
                current = Node(head.val, None, None)
                mapping[head] = current
            prev.next = current
            
            if head.random:
                if not mapping.__contains__(head.random):
                    current.random = Node(head.random.val, None, None)
                    mapping[head.random] = current.random
                else: current.random = mapping[head.random]
            else: current.random = None
                
            prev = current
            head = head.next
        
        return copy_head
        