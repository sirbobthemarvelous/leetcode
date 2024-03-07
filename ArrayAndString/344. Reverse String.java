class Solution {
    public void reverseString(char[] s) {
        char temp = 'a';
        int start = 0;
        int end = s.length-1;
        while(start < end){
            temp = s[start];
            s[start] = s[end];
            s[end] = temp;
            start++;
            end--;
        }
        
    }
}