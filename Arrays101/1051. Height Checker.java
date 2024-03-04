class Solution {
    public int heightChecker(int[] heights) {
        if(heights.length<2) return 0;
        int[] heights2 = heights.clone();
        Arrays.sort(heights2);
        int result = 0;
        for(int x=0; x<heights.length; x++){
            if(heights[x]!=heights2[x]) result++;
        }
        return result;
    }
}