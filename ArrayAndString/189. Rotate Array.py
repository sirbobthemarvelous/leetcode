class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return []
        k %= length
        if k == 0:
            return nums
        def rev(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
    
        rev(0, length-1)  # Reverse the entire array
        rev(0, k-1)  # Reverse the first k elements
        rev(k, length-1)  # Reverse the remaining elements
        
        # let's try faster but more space
        #start = nums[:-k]
        #end = nums[-k:]
        #nums = end+start
        #nums = [y for x in [end, start] for y in x]

        """
        #simple solution
        for x in range(k):
            temp = nums.pop()
            nums.insert(0,temp)
        """
        

