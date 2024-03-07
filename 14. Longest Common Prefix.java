public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String prefix = strs[0];
        for (String s : strs)
            while (s.indexOf(prefix) != 0)
                prefix = prefix.substring(0, prefix.length() - 1);
        return prefix;
    }
}
/*
class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder sb = new StringBuilder();
        for(int i=0; i< strs[0].length();i++){
            for(int s=0; s< strs.length;s++){
                if(i==strs[s].length() || strs[s].charAt(i) != strs[0].charAt(i)) return sb.toString();
                sb.append(strs[0].charAt(i));
            }
        }
        return sb.toString();
        
    }
} */