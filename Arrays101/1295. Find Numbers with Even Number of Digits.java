class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for(int i=0;i<nums.length;i++){
            if((int)(Math.log10(nums[i]))%2 == 1) count++;
            //remember that you're counting evens actually
        }
        return count;
    }
}
/*
huh, this is surprisingly slower than the math solution
class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for(int i=0;i<nums.length;i++){
            if(String.valueOf(nums[i]).length() %2 == 0) count++;
        }
        return count;
    }
}
*/