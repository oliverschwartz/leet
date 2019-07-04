/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return null;
        
        ListNode first = null;
        ListNode current;
        
        if (l1 == null) {
            current = new ListNode(l2.val);
            l2 = l2.next;
        }
        else if (l2 == null) {
            current = new ListNode(l1.val);
            l1 = l1.next;
        }
        else {
            if (l1.val < l2.val) {
                current = new ListNode(l1.val);
                l1 = l1.next;
            }
            else {
                current = new ListNode(l2.val);
                l2 = l2.next;
            }
        }
        first = current;
        
        
        while (l1 != null || l2 != null) {
            // cache smaller value and update pointers
            current.next = new ListNode(0);
            
            if (l1 == null) {
                current.next.val = l2.val;
                l2 = l2.next;
            }
            else if (l2 == null) {
                current.next.val = l1.val;
                l1 = l1.next;
            }
            else if (l2.val < l1.val) {
                current.next.val = l2.val;
                l2 = l2.next;
            }
            else {
                current.next.val = l1.val;
                l1 = l1.next;
            }
            
            current = current.next;
        }   
        
        current.next = null;
        return first;
    }
}
