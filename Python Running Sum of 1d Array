class Solution: #the one I made without help
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        for x in range(len(nums)):
            running += nums[x]
            nums[x] = running
        return nums

"""
def runningSum(self, nums: List[int]) -> List[int]:
	for i in range(1,len(nums)):
		nums[i] = nums[i-1] + nums[i]
	return nums
#leetcode reccomends this since it's in-place
"""