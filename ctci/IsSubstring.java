public class IsSubstring {
    public static boolean isSubstring(String s0, String s1) {
        if (s0.length() != s1.length()) return false;
        else if (s0.length() == 0 && s1.length() == 0) return true;

        /* Duplicate one of the strings. Then, iterate over the
           duplicate string and see if the other string, s0, exists
           anywhere in the duplicated string, s1. */
        s1 += s1;
        for (int i = 0, j = 0; j < s1.length(); j++) {
            if (s0.charAt(i) == s1.charAt(j)) {
                i++;
                if (i == s0.length()) return true;
            }
            else i = 0;
        }
        return false;
    }

    // unit testing
    public static void main(String[] args) {
        // false
        System.out.println(isSubstring("hello", "yo"));
        System.out.println(isSubstring("hello", "hellp"));
        System.out.println(isSubstring("hello", "eello"));
        System.out.println(isSubstring("hello", ""));
        System.out.println(isSubstring("", " "));
        System.out.println();

        // true
        System.out.println(isSubstring("hello", "ohell"));
        System.out.println(isSubstring("hello", "elloh"));
        System.out.println(isSubstring(" ", " "));
        System.out.println(isSubstring("", ""));
        System.out.println(isSubstring("waterbottle", "erbottlewat"));
    }
}