
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