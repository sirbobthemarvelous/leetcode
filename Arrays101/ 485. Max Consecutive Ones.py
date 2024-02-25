class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        started = False
        current = 0
        maxVal = 0
        for x in nums:
            if started:
                if x:
                    current += 1
                else:
                    if maxVal < current:
                        maxVal = current
                    current = 0
                    started = False
            else:
                if x:
                    started = True
                    current = 1
        if maxVal < current:
            return current
        return maxVal
                
"""
Upon Hindsight it looks like I ended up creating something like the Greedy solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, windowSize = 0, 0
        for n in nums:
            if n == 1:
                windowSize += 1
            else:
                res = max(res, windowSize)
                windowSize = 0
        res = max(res, windowSize)

        return res

Sliding Window solution
(Increase size of window if 1, slide it if it's 0)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, zeros = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > 0:
                zeros -= nums[l] == 0
                l += 1
        
        return r - l + 1

Use the Groupy Function
#[k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
#[list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max((len(list(g)) for k, g in groupby(nums) if k == 1), default = 0)

4th solution idea
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, zeros= 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > k: # here k instead of 0
                zeros -= nums[l] == 0
                l += 1
        return r - l + 1