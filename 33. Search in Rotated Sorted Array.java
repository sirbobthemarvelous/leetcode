class Solution {
    public int search(int[] nums, int target) {
        
        int start = 0; 
        int end = nums.length-1;
        
        while(start <= end){
            int mid = start - (start - end)/2; //what about (end-start)/2 - start
            if(nums[mid] == target) return mid; //target just happens to be in the middle
            
            if(nums[start] <= nums[mid]){ //beginning smaller than middle
                if(target >= nums[start] && target <= nums[mid]) end = mid - 1; //lower half
                else start = mid+1;//upper half
            }
            if(nums[mid] <= nums[end]){ // middle smaller than end
                if(target <= nums[end] && target >= nums[mid])  start = mid + 1; //upper half
                else end = mid - 1; //lower half
            }
        }
        //exhaust all options
        return -1;
    }
}