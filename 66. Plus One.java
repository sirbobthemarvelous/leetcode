class Solution {
    public int[] plusOne(int[] digits) {
        if(digits==null||digits.length==0) return new int[0];
        
        int index = digits.length - 1;
        if(digits[index]!=9){
            digits[index] = digits[index]+1;
            return digits;
        }
        while(index>0 && digits[index]==9){
            digits[index]= 0;
            index--;
        }
        if(index==0 && digits[index]==9){
            int[] result = new int[digits.length+1];
            result[0]=1;
            return result;
        }
        else{
            digits[index] = digits[index]+1;
            return digits;
        }
    }
}