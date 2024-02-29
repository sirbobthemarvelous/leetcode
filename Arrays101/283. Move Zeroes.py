class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) < 2): return 
        pointer = 0
        for x in nums:
            if x != 0:
                nums[pointer] = x
                pointer+=1
        while(pointer < len(nums)): 
            nums[pointer] = 0
            pointer+=1


        