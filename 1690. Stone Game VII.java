
class Solution {
    public int stoneGameVII(int[] stones) {
        int bar = stones.length;
        int stonestones[] = new int[bar+1];
        //define the length of the stones and a list of 0, longer than the stones
        
        for(int fib = 0; fib < bar;fib++){
            stonestones[fib+1] = stonestones[fib]+stones[fib];
            //fill the list with the stone values and past stone values
        }
        int[][] states = new int[bar][bar];
        //create a two dimentional list of states
        
        for(int coming=2;coming<bar+1;coming++){
            for(int leaving = 0;leaving<bar-coming+1;leaving++){
                int relayed = leaving+coming-1;
                //the range gets smaller as it goes towards the middle
                states[leaving][relayed] = Math.max(stonestones[relayed+1]-stonestones[leaving+1] - states[leaving+1][relayed],stonestones[relayed]- stonestones[leaving] - states[leaving][relayed-1]);
                //compare taking the left or right rock
            }
        }
        return states[0][bar-1];
        
    }
}