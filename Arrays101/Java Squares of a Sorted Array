class Solution {
    public int[] sortedSquares(int[] nums) {
        /*
        Initialize two pointers (for first and last elements aka left and right pointer)
        create new array to store the result
        loop over array elements from last to first
        compare abs value of left and right pointers
        if abs val of left pointer is >= right pointer, then square left element and put it in the result
        otherwise square right element and store the result
        move pointers towards middle step by step
        do this until pointers have crossed each other.
        */
        int[] out = new int[nums.length];
        for(int i = nums.length - 1, left = 0, right = nums.length - 1; i >= 0; i--){
            out[i] = (nums[left]*nums[left] < nums[right]*nums[right]) ? nums[right]*nums[right--] : nums[left]*nums[left++]; 
            //wow, you did the value returning AND the ++ -- function in teh same line
            //so this is why --variable vs variable-- matters.
        }
        return out;
    }
}