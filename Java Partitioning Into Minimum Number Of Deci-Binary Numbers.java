class Solution {
    public int minPartitions(String n) {
        int tallest = 0;
        char[] splitsy = n.toCharArray();
            // behold a for each loop for arrays
        for (char i: splitsy){
            if ((int) i>tallest) {
                tallest = (int) i;
            }
        }
        return tallest;
    }
}