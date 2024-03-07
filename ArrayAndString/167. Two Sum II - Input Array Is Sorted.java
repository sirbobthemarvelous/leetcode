class Solution {
    public int[] twoSum(int[] numbers, int target) {
        if(numbers.length == 2){
            int[] quick = {1,2};
            return quick;
        } 

        //two pointer solution, but there's probably a binary search solution too.
        int start = 0, end = numbers.length-1;
        int result = numbers[start]+numbers[end];
        while(result != target){
            if(result > target) {
                end -= 1;
            }
            else {
                start +=1;
            }
            result = numbers[start]+numbers[end];
        }
        int[] quick = {start+1,end+1};
        return quick;
    }
}