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

                    
                