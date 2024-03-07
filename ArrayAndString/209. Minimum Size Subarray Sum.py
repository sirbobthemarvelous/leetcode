class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        subLength = float('inf')
        summed = 0
        
        for right in range(len(nums)):
            summed += nums[right]
            #fill up the sum until it's above the target
            
            while summed >= target:
                #update the subaray length
                subLength = min(subLength, right - left + 1)
                #try removing the left side
                summed -= nums[left]
                left += 1
        
        return subLength if subLength != float('inf') else 0
        """
        two pointer
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(sum(nums)< target): return 0
        minSize = len(nums)
        start = 0
        end = len(nums)
        while(start < end and sum(nums[start:end])>=target):
            if(nums[start] <= nums[end-1]):
                start+=1
            else:
                end -= 1
            minSize -=1
        
        return minSize+1
        """