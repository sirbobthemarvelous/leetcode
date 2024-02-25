class Solution {
    public int searchInsert(int[] nums, int target) {
        for(int look = 0;look<nums.length;look++){
            if(nums[look]>= target) return look;
        }
        return nums.length;
    }
}