class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        i = 1
        recorded = nums[0]
        #this would be a great time for a do-while loop
        for x in nums[1::]:
            if x != recorded:
                recorded = x
                nums[i] = x
                i+=1
        return i

        """
        i = 0
        recorded = {}
        for x in nums:
            if x not in recorded:
                recorded[x] = 1
                nums[i] = x
                i+=1
        return i
        """