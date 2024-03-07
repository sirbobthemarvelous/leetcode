class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0,summed = 0;
        int subLength = 100001;
        for(int right=0; right< nums.length; right++){
            summed += nums[right];
            //fill up the sum until it's above the target
            while(summed >= target){
                //update the subarray length
                subLength = Math.min(subLength, right - left + 1);
                //move the array builder to the left side
                summed -= nums[left];
                left++;
            }
        }
        
        if(subLength == 100001) return 0;
        return subLength;
        
    }
}