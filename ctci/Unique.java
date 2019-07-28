public class Unique {
	private final int ASCII = 128;

	public boolean isUnique(String s) {
		if (s.length() > ASCII) return false;

		boolean seen[] = new boolean[ASCII];

		// Iterate over `s`, updating `seen` as we go.
		for (char c : s.toCharArray()) {
			if (seen[c]) return false;
			else seen[c] = true;
		}

		return true;
	}

	public static void main(String[] args) {
		Unique u = new Unique();

		// false
		String s = "hello";
		System.out.println(u.isUnique(s));

		// true
		s = "peanut";
		System.out.println(u.isUnique(s));

		// true
		s = "1234567890qwertyuiopasdfghjklzxcvbnm";
		System.out.println(u.isUnique(s));
	}
}