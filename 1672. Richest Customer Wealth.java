class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxVal = 0;
        for(int x = 0; x < accounts.length; x++){
            int running = 0;
            for(int y = 0; y< accounts[0].length; y++){
                running += accounts[x][y];
            }
            if(running > maxVal){
                maxVal = running;
            }
        }
        return maxVal;
    }
}