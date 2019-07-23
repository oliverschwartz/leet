/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import java.util.HashMap;

public class Solution {
    public boolean hasCycle(ListNode head) {
        // O(1) memory approach: use two pointers.
        // Each iteration, move the 'fast' pointer 2 nodes ahead.
        // Move the 'slow' pointer just one ahead.
        
        if (head == null || head.next == null) return false;
        
        ListNode fast = head.next;
        ListNode slow = head;
        
        while (slow != fast) {
            if (fast == null || fast.next == null) return false;
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}