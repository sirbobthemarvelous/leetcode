class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        """
        nums = sorted(nums)
        result = 0
        for x in range(0,len(nums),2):
            result += nums[x]
        return result
        """
        