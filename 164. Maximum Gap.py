class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        maximum =0
        if len(nums)==1:
            return 0
        
        for index in range(0,len(nums)-1):
            if nums[index+1]-nums[index] > maximum:
                maximum = nums[index+1]-nums[index]
        return maximum
        