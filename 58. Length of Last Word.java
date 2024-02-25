class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        for(int index = s.length(); index >= 1; index--){
            if(s.charAt(index-1) == ' ') return s.length()-index;
        }
        return s.length();
    }
}