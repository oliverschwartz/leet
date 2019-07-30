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
        
        cur = head
        new_head = Node(None, None, None)
        new = new_head
        
        # maps old node => new node
        node_map = {}
        
        # maps an old node we haven't passed yet that is pointed to by a random
        # => a new node missing a random we haven't seen yet
        # 
        # e.g. if we had 1 -> 2 -> 3, and 1.random -> 3, when we pass 1 in the old list
        # we store { 3(old) -> 1(new) }, so when we pass 3 old we know to point the new node
        # previously created to the new node we just created
        #
        missing_randoms = {}

        while cur:
            
            new.next = Node(cur.val, None, None)
            orig_random = cur.random
            
            # current node is pointed to by a past node.random we've created
            if cur in missing_randoms:
                for miss in missing_randoms[cur]:
                    miss.random = new.next
            
            # current node.random points to itself
            if orig_random == cur:
                new.next.random = new.next
              
            # current node.random points to a node we've seen already
            if orig_random in node_map:
                new.next.random = node_map[orig_random]
                
            # we can't set current node.random yet, add to missing
            if cur.random and not new.next.random:
                if cur.random in missing_randoms: missing_randoms[cur.random].append(new.next)
                else: missing_randoms[cur.random] = [new.next]
            
            node_map[cur] = new.next
            new = new.next
            cur = cur.next
        
        return new_head.next