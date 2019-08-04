class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
# Walk along the list; for every node we encounter, 
# check if the node is in the set `seen`. If so, 
# we return that node. If not, we add it to the set
# and continue.
def detectLoop(head):
    if not head:
        return None
    
    # A set to keep track of which nodes we've seen
    seen = set()
    
    while head is not None:
        if head in seen:
            return head
        
        seen.add(head)
        head = head.next
    
    # Would only reach this point if we didn't have a valid list
    # (i.e. a list without a cycle)
    return None         

def main():
    head = Node(1)
    last = Node(5, None)
    n3 = Node(4, last)
    n2 = Node(3, n3)
    n1 = Node(2, n2)
    head.next = n1
    
    print(detectLoop(head))
    
if __name__ == "__main__":
    main()