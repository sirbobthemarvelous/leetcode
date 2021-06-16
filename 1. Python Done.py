class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(0,len(nums)):
            #if nums[index] > target:
                #continue
            #this speedup function doens't work due to negative numbers
            for index2 in range(index+1,len(nums)):
                #if nums[index2] > target:
                    #continue
                if nums[index]+nums[index2]==target:
                    return [index,index2]
                