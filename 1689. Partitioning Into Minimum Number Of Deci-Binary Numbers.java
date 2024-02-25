class Solution {
    public int minPartitions(String n) {
        int max = -1;
        char[] c = n.toCharArray();
        for(int i=0;i<c.length;i++)
        {
            if(max < c[i]-'0')
                max = c[i]-'0';
        }
        return max;
    }
}
"""
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
"""