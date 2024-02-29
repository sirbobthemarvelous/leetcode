class Solution {
    public int[] sortArrayByParity(int[] nums) {
        if(nums.length < 2) return nums;
        //two pointer solution
        int i = 0;                  // Initialize the first pointer at the beginning of the array.
        int j = nums.length - 1;    // Initialize the second pointer at the end of the array.
        int temp;

        while (i < j) {
            if (nums[i] % 2 == 0) {  // If nums[i] is even, increment i.
                i++;
            } else if (nums[j] % 2 != 0) {  // If nums[j] is odd, decrement j.
                j--;
            } else {  // If nums[i] is odd and nums[j] is even, swap them and update pointers.
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--;
            }
        }

        return nums;
        /*
        int left = 0;
        int temp;
        for(int right = nums.length-1; right > -1; right--){
            if(right%2==0) {
                temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
            }
        }
        return nums;
        */
    }
}