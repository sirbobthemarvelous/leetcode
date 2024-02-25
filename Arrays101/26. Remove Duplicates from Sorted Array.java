class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length==1) return 1;
        int i = 1;

        for(int x = 1; x < nums.length; x++){
            if(nums[x] != nums[i-1]){
                nums[i] = nums[x]; //unlike python, java is faster at recalling than storing
                i++;
            }
        }
        return i;
        
    }
}