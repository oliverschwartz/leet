import java.util.HashMap;

public class RemoveDuplicatesUnsortedList {
    public static class Node {
        Node next;
        int val;

        public Node(Node next, int val) {
            this.next = next;
            this.val = val;
        }
    }

    public static Node removeDups(Node head) {
        HashMap<Integer, Integer> freqs = new HashMap<Integer, Integer>();

        Node n = head;
        
        // Get the frequencies of all values and store them in a hashtable.
        while (n != null) {
            if (freqs.containsKey(n.val))
                freqs.put(n.val, freqs.get(n.val) + 1);
            else 
                freqs.put(n.val, 1);
            n = n.next;
        }

        Node prev = head;
        n = head;

        // Iterate over the list, removing any nodes that appear more than once.
        while (n != null) {
            if (freqs.get(n.val) > 1) {
                if (n == head) {
                    head = n.next;
                    prev = head;
                    n = head;
                }
                else {
                    prev.next = n.next;
                    n = n.next;
                }
            }
            else {
                prev = n;
                n = n.next;
            }
        }
        
        return head;
    }

    public static void printList(Node head) {
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // build list: 1 -> 2 -> 3 -> 2 -> 1 (in reverse)
        Node n4 = new Node(null, 1);
        Node n3 = new Node(n4, 2);
        Node n2 = new Node(n3, 3);
        Node n1 = new Node(n2, 2);
        Node head = new Node(n1, 1);

        // 1, 2, 3, 2, 1
        printList(head);

        head = removeDups(head);

        // 3
        printList(head);

        // build list: 1 -> 1
        Node last = new Node(null, 1);
        head = new Node(last, 1);

        // 1, 1
        printList(head);
        
        head = removeDups(head);
        
        // no output
        printList(head);
    }
}