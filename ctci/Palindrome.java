import java.lang.StringBuilder;

public class Palindrome {
	Node head;

	public Palindrome() {
		Node<Integer> last = new Node<Integer>(null, 0);
		Node<Integer> n3 = new Node<Integer>(last, 1);
		Node<String> n2 = new Node<String>(n3, "32");
		Node<Integer> n1 = new Node<Integer>(n2, 123);
		Node<Integer> head = new Node<Integer>(n1, 0);
		this.head = head;
	}


	public class Node<Value> {
		Node next;
		Value val;

		public Node(Node next, Value val) {
			this.next = next;
			this.val = val;
		}
	}

	public boolean isPalindrome(Node head) {
		StringBuilder sb = new StringBuilder();

		while (head != null) {
			sb.append(head.val.toString());
			head = head.next;
		}

		String s = sb.toString();

		for (int i = 0; i < s.length() / 2; i++) {
			int j = s.length() - i - 1;
			if (s.charAt(i) != s.charAt(j))
				return false;
		}

		return true;
	}

	public static void main(String[] args) {
		Palindrome p = new Palindrome();

		System.out.println(p.isPalindrome(p.head));
	}
}