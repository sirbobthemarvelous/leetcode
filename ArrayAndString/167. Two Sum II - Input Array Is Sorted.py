class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if(len(numbers) == 2): return [1,2]

        #two pointer solution, but there's probably a binary search solution too.
        start = 0
        end = len(numbers)-1
        result = numbers[start]+numbers[end]
        while(result != target):
            if(result > target):
                end -= 1
            else:
                start +=1
            result = numbers[start]+numbers[end]
        return [start+1,end+1]
        

        