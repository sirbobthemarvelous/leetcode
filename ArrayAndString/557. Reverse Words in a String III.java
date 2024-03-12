class Solution {
    public String reverseWords(String s) {
        int i = 0;
        char[] arr = s.toCharArray();
        int len = s.length();
        while(i < len){
            //skip over the whitespace
            if(arr[i] == ' '){
                i++;
            }
            //find the end of the first word
            int k = i;
            while(k < len && arr[k] != ' '){
                k++;
            }
            // swap the first word
            int n = k - 1;
            while(i < n){
                char t = arr[n];
                arr[n] = arr[i];
                arr[i] = t;
                n--;
                i++;
            }
            i = k;
            //move on to the next
        }
        return new String(arr);
    }
    /*
    slower but less memory
    public String reverseWords(String s) {
        StringBuffer sb = new StringBuffer();
        String[] arr = s.split(" ");
        for(int i=0; i<arr.length; i++){
            if(i==arr.length-1){
                sb.append(reverse(arr[i]));
            }else{
                sb.append(reverse(arr[i])+" ");
            }
        }
        return sb.toString();
    }
    String reverse(String s){
        StringBuffer sb = new StringBuffer();
        return sb.append(s).reverse().toString();
    }

    */
}