class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} #hash map
        for i,n in enumerate(nums):
            if n in dict:
                return dict[n],i
            else:
                dict[target-n]=i #dictionary of complements
        
"""
    for index in range(0,len(nums)):
            #if nums[index] > target:
                #continue
            #this speedup function doens't work due to negative numbers
            for index2 in range(index+1,len(nums)):
                #if nums[index2] > target:
                    #continue
                if nums[index]+nums[index2]==target:
                    return [index,index2]
                """