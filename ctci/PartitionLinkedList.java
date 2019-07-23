/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head == null) return null;
        else if (head.next == null) return head;

        // If the first element in the list is greater than or equal
        // to x, we insert elements before `head`.
        boolean insertAtHead = (head.val >= x) ? true : false;
        
        // Find the spot 1 before a node larger than or equal to x.
        // We will insert smaller nodes than x, after this `left` node.
        ListNode left = head;
        while ((left.val < x && left.next != null) && left.next.val < x)
            left = left.next;
        if (left.next == null) return head;
        
        // Starting the element after `left`, stop every time we find an
        // element less than x. Move this node to be 1 node after left.
        ListNode right = left.next;
        ListNode prev = left;
        while (right != null) {
            ListNode tmp = right.next;
            
            if (right.val < x) {
                if (insertAtHead) {
                    prev.next = right.next;
                    right.next = head;
                    head = right;
                    left = head;
                    insertAtHead = false;
                    right = tmp;
                }
                else {
                    prev.next = right.next;
                    right.next = left.next;
                    left.next = right;
                    left = left.next;
                    right = tmp;
                }
            }
            else {
                prev = right;
                right = right.next;
            }
        }
        
        return head;
    }
}