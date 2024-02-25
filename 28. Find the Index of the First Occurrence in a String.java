class Solution {
    public int strStr(String haystack, String needle) {
        int size = needle.length();
        for(int index = 0; index < haystack.length()-size+1;index++){
            if(needle.equals(haystack.substring(index,index+size))){
                return index;
            }
        }
        return -1;
    }
}