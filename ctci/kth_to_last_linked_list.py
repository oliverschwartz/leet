class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def listify(lst):
    head = ListNode(lst[0])
    cur = head
    for i in range(1, len(lst)):
        cur.next = ListNode(lst[i])
        cur = cur.next
    return head

def kth_to_last(head, k):
    slow = head
    fast = head
    for i in range(k - 1):
        fast = fast.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    return slow.val


l = listify([1, 2, 3, 4, 5, 6, 7])
assert kth_to_last(l, 2) == 6
assert kth_to_last(l, 1) == 7
assert kth_to_last(l, 3) == 5
