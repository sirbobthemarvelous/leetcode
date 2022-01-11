class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [] #we're just going to brute force this array
        for index in range(0,len(nums)-1):
            aboves = 0
            for checking in range(index+1,len(nums)):
                if nums[checking] < nums[index]:
                    aboves += 1
            counts.append(aboves)
        counts.append(0)
        return counts
        #https://kennyzhuang.gitbooks.io/algorithms-collection/content/count_of_smaller_numbers_after_self.html