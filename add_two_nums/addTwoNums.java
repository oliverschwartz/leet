/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        // set a pointer to the front of the linked list,
        // as well as a pointer to the current node
        ListNode first = null, current = null;
        int sum, sumBit, carryBit = 0;
        
        // iterate until we have reached the end of both lists
        while (l1 != null | l2 != null) {
            
            // if we have reached the end of one number
            if (l1 == null)
                sum = l2.val + carryBit;
            else if (l2 == null)
                sum = l1.val + carryBit;
            
            // both numbers still have digits
            else 
                sum = l1.val + l2.val + carryBit;
            
            sumBit = sum % 10;
            carryBit = sum / 10;
            
            // create nodes in the linked list
            if (first == null) {
                first = new ListNode(sumBit);
                current = first;
            }
            else {
                current.next = new ListNode(sumBit);
                current = current.next;
            }
            
            // update pointers 
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        
        // if the carry is non-zero, create a final node
        if (carryBit > 0) {
            current.next = new ListNode(carryBit);
            current.next.next = null;
        }
        
        return first;
    }
}



