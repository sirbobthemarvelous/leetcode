class Solution(object):
    def maximumUniqueSubarray(self, nums):
        point1 = 0
        point2 = len(nums)-1
        biggest = 0
        #use for loops and jumping for substrings, like when you see a duplicate jump both points
        for index, value in enumerate(nums):
            
        """
        :type nums: List[int]
        :rtype: int
        """
        