class Solution {
    public int dominantIndex(int[] nums) {
        //fast but not the most space efficient
        int second = 0, maxVal = 0, maxIndex=0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] > maxVal){
                second = maxVal;
                maxVal = nums[i];
                maxIndex = i;
            }
            else if(nums[i]>second) second = nums[i];
        }
        if(maxVal >= second*2) return maxsIndex;

        return -1;
    }
}