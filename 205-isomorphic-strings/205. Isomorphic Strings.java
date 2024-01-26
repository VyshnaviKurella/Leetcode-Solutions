class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Character> map1 = new HashMap<>();
        Map<Character, Character> map2 = new HashMap<>();
        
        for(int i = 0; i < s.length(); i++) {
            char charInS = s.charAt(i);
            char charInT = t.charAt(i);
            
            if(map1.containsKey(charInS) && map1.get(charInS) != charInT) {
                return false;
            }
            
            if(map2.containsKey(charInT) && map2.get(charInT) != charInS) {
                return false;
            }
            
            map1.put(charInS, charInT);
            map2.put(charInT, charInS);
        }
        return true;
    }
}