class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1
        nums = sorted(nums)
        chunk = 1
        #remove duplicates
        nums = list(dict.fromkeys(nums))
        for index in range(1,len(nums)):
            if nums[index-1] == nums[index]-1:
                chunk+=1
            else:
                if chunk > longest:
                    longest = chunk
                chunk=1
        if chunk > longest:
                longest = chunk
                
        return longest