class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int extra = 0;
        int aLength = a.length()-1;
        int bLength = b.length()-1;
        while(aLength >=0 || bLength >= 0 || extra == 1){
            if(aLength >= 0){
                extra += a.charAt(aLength) - '0';
                aLength--;
            }
            if(bLength >= 0){
                extra += b.charAt(bLength) - '0';
                bLength--;
            }
            sb.append(extra %2);
            extra /= 2;
        }
        return sb.reverse().toString();
    }
}