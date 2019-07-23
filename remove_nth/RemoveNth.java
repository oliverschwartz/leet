/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        // One pass algorithm: move one pointer n nodes ahead.
        // Then, until the `front` pointer reaches the end,
        // advance both pointers by one. 
        // Then, the `back` pointer will be pointing
        // at the node one before the node to be removed.
        ListNode front = head;
        ListNode back  = head;
        
        for (int i = 0; i < n; i++) {
            front = front.next;
        }
        if (front == null)  {
            head = head.next;
            return head;
        }
        
        while (front.next != null) {
            front = front.next;
            back = back.next;
        }
        
        back.next = back.next.next;
        return head;
    }
}