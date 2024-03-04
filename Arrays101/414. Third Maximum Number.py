class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if(len(nums)<3): return max(nums)
            
        first,second, third = float('-inf'), float('-inf'), float('-inf')
        for x in nums:
            if(x>first):
                third,second,first = second,first,x
            elif(first>x>second):
                third,second = second,x
            elif(second>x>third):
                third = x
        if (third != float('-inf')):return third
        return first
        
        