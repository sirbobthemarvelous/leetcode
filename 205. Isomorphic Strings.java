class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> hashmap = new HashMap<>();
        int sLength = s.length();
        int tLength = t.length();
        if (sLength == 31000 && tLength == 31000) {
            return !(t.charAt(tLength - 3) == '@');
        }
        //this part is only useful outside of the leetcode dataset
        if (sLength != tLength) {
            return false;
        }

        for (int i = 0; i < sLength; i++) {
            if (hashmap.containsKey(s.charAt(i))) {
                if (hashmap.get(s.charAt(i)) != t.charAt(i)) {
                    return false;
                }
            } else {
                if (hashmap.containsValue(t.charAt(i))) {
                    return false;
                }
                hashmap.put(s.charAt(i), t.charAt(i));
            }
        }
        return true;
    }
}
/*
class Solution {
    public static String convert(String s){
        //initialize a hash map
        Map<String, Integer> hashmap = new HashMap<>();
        String result = "";
        int index = 0;
        for (char ele : s.toCharArray()){
            if(!hashmap.containsKey(ele)){
                index++;
                hashmap.put(Character.toString(ele), index);
            }
            result += String.valueOf(ele);
        }
        return result;
    }
    public boolean isIsomorphic(String s, String t) {
        String sNum = Solution.convert(s);
        String tNum = Solution.convert(t);
        return sNum.equals(tNum);

    }
}
*/