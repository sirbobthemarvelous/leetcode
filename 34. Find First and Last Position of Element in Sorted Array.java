class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = binarySearch(nums,0,nums.length-1,target);
        int[] result = {first,first};
        if(first == -1) return result;
        int last = first;
        while(first >0 && nums[first-1] == target){
            first--;
        }
        while(last < nums.length-1 && nums[last+1] == target ){
            last++;
        }
        result[0] = first;
        result[1] = last;
        return result;
    }
    public int binarySearch(int[] nums, int begin, int end, int target){
        if(begin == end && nums[begin]!=target) return -1;
        int mid = (begin+end)/2;
        if(mid<0 || mid>nums.length-1) return -1;
        if(nums[mid]==target) return mid;
        if(nums[mid]>target) return binarySearch(nums,begin,mid,target);
        else return binarySearch(nums,mid+1,end,target);
    }
}