import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if(int(math.log10(x))%2): count += 1 # you're counting every odd, so you want to move the number by 1
            
        return count
        
        """
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([x for x in nums if len(str(x)) % 2 == 0])

        list comprehension is approximately as fast in this usecase
        """        
        