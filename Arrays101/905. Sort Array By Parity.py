class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if(len(nums) < 2): return nums
        # list comprehensions solution
        evens = [x for x in nums if x%2==0]
        odds = [x for x in nums if x%2==1]
        return evens+odds
        
        """
        #two-pointer solution
        i, j = 0, len(nums) - 1
        
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1
            while i < j and nums[j] % 2 == 1:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
        
        return nums
        
        """