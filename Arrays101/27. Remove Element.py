class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        #yeah the twopointer solution is way faster
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
        """
        result = len(nums)
        places = []
        for x in range(result):
            if nums[x] == val: 
                places.append(x)
                result -=1
        for num in reversed(places):
            nums.pop(num)
        return result
        """
        
