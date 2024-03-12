class Solution {
    public void rotate(int[] nums, int k) {
        int length = nums.length;
        k = k % length;
        if(k == 0 || length == 1) return;
        int[] start = Arrays.copyOfRange(nums, 0, length-k);
        int[] end = Arrays.copyOfRange(nums, length-k, nums.length);
        System.arraycopy(end, 0, nums, 0, end.length);          
        System.arraycopy( start, 0, nums, end.length, start.length );
        //alright lesson of the day, Built-in Java methods are your friend
    }
}