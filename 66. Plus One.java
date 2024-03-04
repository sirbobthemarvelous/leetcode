class Solution {
    public int[] plusOne(int[] digits) {
        int length = digits.length-1;
        if(digits[length]!=9){
            digits[length]++;
            return digits;
        }
        for(int i=length; i>-1;i--){
            if(digits[i]==9){
                digits[i]=0;
            }
            else {
                digits[i]++;
                return digits;
            }
        }
        digits = new int[length + 2];
        digits[0] = 1;
        return digits;
        /*
        int[] result = new int[length+1];
        result[0]=1;
        for(int i = 1; i< length+1;i++){
            result[i] = digits[i-1];
        }
        
        int i = 1;
        for(int ele: digits){
            result[i] = ele;
            i++;
        }
        return result;
        */
    }
}