/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public int numComponents(ListNode head, int[] G) {
        int count = 0; 
        boolean inComponent = false;
        
        while (head != null) {
            if (!inComponent) {
                if (inArray(head.val, G)) {
                    count++;
                    inComponent = true;
                }
            }
            else if (!inArray(head.val, G))
                inComponent = false;
            head = head.next;
        }
        return count;
    }
    
    // check if target is in G
    private boolean inArray(int target, int[] G) {
        for (int i = 0; i < G.length; i++)
            if (G[i] == target) return true;
        return false;
    }
}
