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
        // Brute-force: cache all nodes seen so far.
        // For each node, check if we have seen it before.
        HashMap<ListNode, Boolean> seen = new HashMap<ListNode, Boolean>();
        
        while (head != null) {
            if (seen.containsKey(head)) return true;
            else seen.put(head, true);
            head = head.next;
        }
        
        return false;
    }
}