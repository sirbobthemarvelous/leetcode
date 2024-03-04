class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #minimal space
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -1 * abs(nums[idx])
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
        
        """
        #list comprehension, for speed
        result = range(1,len(nums)+1)
        nums = set(nums)
        result = [x for x in result if x not in nums]
        return result
        """

        