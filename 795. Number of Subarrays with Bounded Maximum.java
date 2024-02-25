class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        return countBelowBoundary(nums, right)-countBelowBoundary(nums,left-1);
    }
    
 
    public int countBelowBoundary(int[] A, int bound){
        int count = 0;
        int temp = 0;
 
        for(int a: A){
            if(a<=bound){
                temp = temp +1;
                count += temp;
            }else{
                temp = 0;
            }
        }
        return count;
    }
}