class Solution {
    public void moveZeroes(int[] nums) {
        //check edge cases
        if(nums.length < 2) return;
        int pointer = 0;
        for(int x = 0; x<nums.length;x++){
            if(nums[x]!=0){
                nums[pointer] = nums[x];
                pointer++;
            }
        }
        while(pointer <nums.length){
            nums[pointer] = 0;
            pointer++;
        }
    }
}