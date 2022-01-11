class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        #find the largest value in the list, and make lists with it and any surrounding indexes
        def checkAhead(index: int) -> int:
            ayys2=0
            goingLeft=0
            goingRight=0
            for center in range(index, len(nums)):
                if left<= nums[center] <=right: #checking each individual array
                    ayys2+= 1
                if not center==0: #check the potential subarrays to the left
                    for backlog in range(center, 0,-1):
                        if not nums[backlog] <=right:
                            break
                        goingLeft +=1
                if not center==len(nums)-1: #check the potential subarrays to the right
                    for frontlog in range(center, 0,-1):
                        if not nums[frontlog] <=right:
                            break
                        if left<= nums[frontlog] <=right:
                            break # prevent duplicates
                        goingRight +=1
                ayys2 += goingLeft*goingRight
                    #no you need to check left and right and Multiply
                    #im still getting duplicates though
            return ayys2
        return checkAhead(0)
                    
                    
                