class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def belowBoundary(nums: List[int], boundary: int)-> int:
            ayys = 0
            pyramidBonus = 0 # we're counting more than just the individual numbers as subarrays
            
            for check in range(0,len(nums)):
                if nums[check]<=boundary:
                    pyramidBonus = pyramidBonus+1
                    ayys += pyramidBonus
                else:
                    pyramidBonus=0
                    
            return ayys
        return belowBoundary(nums,right)-belowBoundary(nums,left-1)
        """public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        return countBelowBoundary(nums, right)-countBelowBoundary(nums,left-1);
    }
    // looks like the trick is to convert the list into Binary boundaries and Count Below the boundaries
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
    }"""
                    
                