class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = 0
        for index, ele in enumerate(nums):
            sum1 -= ele
            if(sum1 == sum2): return index
            sum2+= ele

        return -1
        """
        #more space efficient
        sum1 = sum(nums)
        sum2 = 0
        past = 0
        index = 0
        for x in nums:
            sum2 += past
            sum1 -= x
            if(sum1 == sum2): return index
            past = x
            index +=1

        return -1
        """