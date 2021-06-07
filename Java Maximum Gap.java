class Solution {
    public int maximumGap(int[] nums) {
        if(nums.length ==1){
            return 0;
        }
        int maximum =0;
        Arrays.sort(nums);
        for(int index=0; index<nums.length-1;index++){
            if(nums[index+1]-nums[index] > maximum){
                maximum = nums[index+1]-nums[index];
            }
        }
        return maximum;
    }
}