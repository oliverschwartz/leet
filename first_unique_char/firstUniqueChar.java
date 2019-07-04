import java.util.HashMap;

class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> h = new HashMap<Character, Integer>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (h.containsKey(c)) h.put(c, h.get(c) + 1);
            else h.put(c, 1);
        }
        
        ArrayList<Character> sols = new ArrayList<Character>();
        for (char c : h.keySet())
            if (h.get(c) == 1) sols.add(c);

        int champ = -1;
        for (int i = 0; i < sols.size(); i++) {
            if (i == 0) champ = s.indexOf(sols.get(i));
            else {
                int index = s.indexOf(sols.get(i));
                if (index < champ) champ = index;
            }
        }
        return champ;
    }
}