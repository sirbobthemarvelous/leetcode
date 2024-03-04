class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0; //fill left with the sum of the whole string
        for(int ele: nums) left += ele;

        int right = 0;
        for(int i=0; i< nums.length;i++){
            left -= nums[i];
            if(left == right) return i;
            right += nums[i];
        }
        return -1;
        
    }
}