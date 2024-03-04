class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        second = 0
        maxVal = 0
        for val in nums:
            if (val > maxVal):
                second = maxVal
                maxVal = val
            elif(val > second):
                second = val

        if(maxVal >= 2*second): return nums.index(maxVal)

        return -1
        """
        second = 0
        maxVal = 0
        maxIndex = 0
        for index,val in enumerate(nums):
            if (val > maxVal):
                second = maxVal
                maxVal = val
                maxIndex = index
            elif(val > second):
                second = val

        if(maxVal >= 2*second): return maxIndex

        return -1
        """