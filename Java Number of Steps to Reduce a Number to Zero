import java.math.BigInteger;  
//took a bit of methodfinding but here is bitmanipulation solution in java
class Solution {
    public int numberOfSteps(int num) {
        if(num == 0) return 0;
        return BigInteger.valueOf(num).bitLength() -1 + Integer.bitCount(num);
        
    }
}