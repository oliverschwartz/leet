import java.lang.Math;

public class OneAway {
	public boolean oneAway(String s0, String s1) {
		if (s0.length() != s1.length() && Math.abs(s0.length() - s1.length()) != 1)
			return false;

		// check for replacement
		if (s0.length() == s1.length()) {
			int diff = 0;

			for (int i = 0; i < s0.length(); i++) {
				if (diff > 1) return false;
				if (s0.charAt(i) != s1.charAt(i)) diff++;
			}
			return diff == 1;
		}
		else { // check for insertion/deletion
			boolean foundMismatch = false;
			int l = 0; 
			int s = 0;

			String s_long = s0.length() < s1.length() ? s1 : s0;
			String s_short = s0.length() < s1.length() ? s0 : s1;

			for (; s < s_short.length(); s++) {
				if (s_long.charAt(l) != s_short.charAt(s)) {
					if (foundMismatch) return false;
					foundMismatch = true;
					l++;
				}
				l++;
			}
			return true;
		}
	}

	public static void main(String[] args) {
		OneAway oa = new OneAway();

		// true
		System.out.println(oa.oneAway("pale", "ple"));
		System.out.println(oa.oneAway("ple", "pale"));
		System.out.println(oa.oneAway("pales", "pale"));
		System.out.println(oa.oneAway("pales", "paless"));
		System.out.println(oa.oneAway("hello", "helllo"));

		// false
		System.out.println(oa.oneAway("hello", "hello"));
		System.out.println(oa.oneAway("pale", "bake"));
		System.out.println(oa.oneAway("", ""));
	}
}